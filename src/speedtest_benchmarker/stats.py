"""Summary statistics over a set of results."""

from __future__ import annotations

import csv
import statistics
from dataclasses import asdict
from pathlib import Path

from .runner import FIELDS, Result

_NUMERIC = [
    "server_id", "latency_ms", "jitter_ms", "download_mbps", "upload_mbps",
    "download_mb", "upload_mb", "packet_loss", "duration_s",
]


def append_csv(path: Path, result: Result) -> None:
    new = not path.exists() or path.stat().st_size == 0
    with path.open("a", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS)
        if new:
            writer.writeheader()
        writer.writerow(asdict(result))


def read_csv(path: Path) -> list[Result]:
    with path.open(newline="", encoding="utf-8") as fh:
        rows = []
        for row in csv.DictReader(fh):
            for key in _NUMERIC:
                row[key] = int(row[key]) if key == "server_id" else float(row[key])
            rows.append(Result(**row))
    return rows


def _describe(values: list[float]) -> dict[str, float]:
    return {
        "mean": statistics.fmean(values),
        "median": statistics.median(values),
        "min": min(values),
        "max": max(values),
    }


def summarize(results: list[Result]) -> dict:
    """Aggregate stats. Raises ValueError on an empty list."""
    if not results:
        raise ValueError("no results to summarize")
    return {
        "tests": len(results),
        "servers": len({r.server_id for r in results}),
        "data_mb": sum(r.download_mb + r.upload_mb for r in results),
        "latency_ms": _describe([r.latency_ms for r in results]),
        "jitter_ms": _describe([r.jitter_ms for r in results]),
        "download_mbps": _describe([r.download_mbps for r in results]),
        "upload_mbps": _describe([r.upload_mbps for r in results]),
        "packet_loss": _describe([r.packet_loss for r in results]),
        "duration_s": _describe([r.duration_s for r in results]),
    }


def format_summary(summary: dict, plan: tuple[float, float] | None = None) -> str:
    def row(label: str, key: str, unit: str) -> str:
        s = summary[key]
        return (f"  {label:<12}{s['mean']:>9.2f}{s['median']:>9.2f}"
                f"{s['min']:>9.2f}{s['max']:>9.2f}  {unit}")

    lines = [
        f"{summary['tests']} tests across {summary['servers']} servers "
        f"({summary['data_mb'] / 1000:.2f} GB transferred)",
        "",
        f"  {'':<12}{'mean':>9}{'median':>9}{'min':>9}{'max':>9}",
        row("Download", "download_mbps", "Mbps"),
        row("Upload", "upload_mbps", "Mbps"),
        row("Latency", "latency_ms", "ms"),
        row("Jitter", "jitter_ms", "ms"),
        row("Packet loss", "packet_loss", "%"),
    ]
    if plan:
        down, up = plan
        lines += [
            "",
            f"Versus your {down:g}/{up:g} Mbps plan (median):",
            f"  Download  {summary['download_mbps']['median'] / down * 100:.1f}%",
            f"  Upload    {summary['upload_mbps']['median'] / up * 100:.1f}%",
        ]
    return "\n".join(lines)
