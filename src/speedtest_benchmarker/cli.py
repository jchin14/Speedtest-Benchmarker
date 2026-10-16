"""Command line interface."""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

from . import __version__
from .runner import Result, SpeedtestError, list_servers, run_test
from .stats import append_csv, format_summary, read_csv, summarize


def parse_plan(text: str) -> tuple[float, float]:
    try:
        down, up = (float(p) for p in text.split("/"))
        if down <= 0 or up <= 0:
            raise ValueError
    except ValueError:
        raise argparse.ArgumentTypeError("plan must look like 250/25 (Mbps down/up)") from None
    return down, up


def parse_servers(text: str) -> list[int]:
    try:
        return [int(p) for p in text.replace(",", " ").split()]
    except ValueError:
        raise argparse.ArgumentTypeError("servers must be a comma separated list of IDs") from None


def read_servers_file(path: Path) -> list[int]:
    ids: list[int] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if line:
            ids.extend(parse_servers(line))
    return ids


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="speedtest-benchmarker",
        description="Benchmark your connection against many Speedtest servers.",
    )
    p.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = p.add_subparsers(dest="command", required=True)

    run = sub.add_parser("run", help="run tests and record them to a CSV")
    target = run.add_mutually_exclusive_group()
    target.add_argument("-s", "--servers", type=parse_servers, metavar="IDS",
                        help="comma separated server IDs to test")
    target.add_argument("-f", "--servers-file", type=Path, metavar="FILE",
                        help="file of server IDs (one or more per line, # comments)")
    target.add_argument("-n", "--nearby", type=int, metavar="N",
                        help="test the N nearest servers")
    run.add_argument("-r", "--rounds", type=int, default=1, metavar="N",
                     help="repeat the whole server list N times (default 1)")
    run.add_argument("-i", "--interval", type=float, default=1.0, metavar="SEC",
                     help="pause between tests (default 1s)")
    run.add_argument("-o", "--output", type=Path, default=Path("results.csv"),
                     help="CSV to append to (default results.csv)")
    run.add_argument("--plan", type=parse_plan, metavar="DOWN/UP",
                     help="your plan speed in Mbps, e.g. 250/25")
    run.add_argument("--timeout", type=float, default=180,
                     help="per-test timeout in seconds (default 180)")

    rep = sub.add_parser("report", help="summarize an existing results CSV")
    rep.add_argument("file", type=Path)
    rep.add_argument("--plan", type=parse_plan, metavar="DOWN/UP")

    srv = sub.add_parser("servers", help="list the nearest servers and their IDs")
    srv.add_argument("-n", "--limit", type=int, default=10)
    return p


def _line(i: int, total: int, r: Result) -> str:
    return (f"[{i}/{total}] {r.server_name} ({r.location}, {r.country}) "
            f"id={r.server_id}  down {r.download_mbps:.1f}  up {r.upload_mbps:.1f} Mbps  "
            f"ping {r.latency_ms:.1f} ms")


def cmd_run(args: argparse.Namespace) -> int:
    if args.rounds < 1:
        print("error: --rounds must be at least 1", file=sys.stderr)
        return 2
    if args.servers_file:
        servers: list[int | None] = list(read_servers_file(args.servers_file))
    elif args.nearby:
        servers = [s["id"] for s in list_servers()[: args.nearby]]
    elif args.servers:
        servers = list(args.servers)
    else:
        servers = [None]  # let the CLI pick the closest
    if not servers:
        print("error: no servers to test", file=sys.stderr)
        return 2

    plan = [s for _ in range(args.rounds) for s in servers]
    results: list[Result] = []
    failures = 0
    try:
        for i, server in enumerate(plan, 1):
            try:
                result = run_test(server, args.timeout)
            except SpeedtestError as exc:
                failures += 1
                print(f"[{i}/{len(plan)}] server {server}: failed ({exc})", file=sys.stderr)
                if server is None:  # CLI missing or offline, retrying won't help
                    return 1
                continue
            append_csv(args.output, result)
            results.append(result)
            print(_line(i, len(plan), result))
            if i < len(plan):
                time.sleep(args.interval)
    except KeyboardInterrupt:
        print("\nInterrupted.")

    if not results:
        print("No successful tests.", file=sys.stderr)
        return 1
    print(f"\nSaved {len(results)} results to {args.output}"
          + (f" ({failures} failed)" if failures else "") + "\n")
    print(format_summary(summarize(results), args.plan))
    return 0


def cmd_report(args: argparse.Namespace) -> int:
    try:
        results = read_csv(args.file)
        print(format_summary(summarize(results), args.plan))
    except (OSError, KeyError, ValueError, TypeError) as exc:
        print(f"error: could not read {args.file}: {exc}", file=sys.stderr)
        return 1
    return 0


def cmd_servers(args: argparse.Namespace) -> int:
    for s in list_servers()[: args.limit]:
        print(f"{s['id']:>7}  {s['name']} - {s['location']}, {s['country']}")
    return 0


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    handler = {"run": cmd_run, "report": cmd_report, "servers": cmd_servers}[args.command]
    try:
        return handler(args)
    except SpeedtestError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
