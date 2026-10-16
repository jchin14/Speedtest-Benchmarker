"""Run the Ookla Speedtest CLI and parse its JSON output."""

from __future__ import annotations

import json
import shutil
import subprocess
import time
from dataclasses import dataclass, fields


class SpeedtestError(RuntimeError):
    """The Speedtest CLI is missing or a test failed."""


@dataclass
class Result:
    timestamp: str
    server_id: int
    server_name: str
    location: str
    country: str
    isp: str
    latency_ms: float
    jitter_ms: float
    download_mbps: float
    upload_mbps: float
    download_mb: float
    upload_mb: float
    packet_loss: float
    duration_s: float
    result_url: str


FIELDS = [f.name for f in fields(Result)]


def _mbps(bytes_per_second: float) -> float:
    return bytes_per_second * 8 / 1_000_000


def _mb(num_bytes: float) -> float:
    return num_bytes / 1_000_000


def find_cli() -> str:
    path = shutil.which("speedtest")
    if path is None:
        raise SpeedtestError(
            "Ookla Speedtest CLI not found on PATH. "
            "Install it from https://www.speedtest.net/apps/cli"
        )
    return path


def _command(server_id: int | None = None, list_servers: bool = False) -> list[str]:
    cmd = [find_cli(), "-f", "json", "--accept-license", "--accept-gdpr"]
    if list_servers:
        cmd.append("--servers")
    elif server_id is not None:
        cmd += ["--server-id", str(server_id)]
    return cmd


def _run_json(cmd: list[str], timeout: float) -> dict:
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired as exc:
        raise SpeedtestError(f"timed out after {timeout:.0f}s") from exc
    # The CLI prints JSON error objects to stdout/stderr and exits non-zero.
    for line in reversed((proc.stdout + "\n" + proc.stderr).splitlines()):
        line = line.strip()
        if line.startswith("{"):
            try:
                data = json.loads(line)
            except json.JSONDecodeError:
                continue
            if data.get("type") == "log" and data.get("level") == "error":
                raise SpeedtestError(data.get("message", "unknown error"))
            return data
    raise SpeedtestError((proc.stderr or proc.stdout).strip() or "no output from speedtest")


def parse_result(data: dict, duration_s: float) -> Result:
    try:
        server = data["server"]
        return Result(
            timestamp=data["timestamp"],
            server_id=int(server["id"]),
            server_name=server["name"],
            location=server["location"],
            country=server["country"],
            isp=data["isp"],
            latency_ms=data["ping"]["latency"],
            jitter_ms=data["ping"]["jitter"],
            download_mbps=_mbps(data["download"]["bandwidth"]),
            upload_mbps=_mbps(data["upload"]["bandwidth"]),
            download_mb=_mb(data["download"]["bytes"]),
            upload_mb=_mb(data["upload"]["bytes"]),
            packet_loss=data.get("packetLoss", 0.0),
            duration_s=duration_s,
            result_url=data.get("result", {}).get("url", ""),
        )
    except (KeyError, TypeError) as exc:
        raise SpeedtestError(f"unexpected speedtest output (missing {exc})") from exc


def run_test(server_id: int | None = None, timeout: float = 180) -> Result:
    """Run one test. With no server_id the CLI picks the closest server."""
    start = time.monotonic()
    data = _run_json(_command(server_id), timeout)
    return parse_result(data, round(time.monotonic() - start, 2))


def list_servers(timeout: float = 60) -> list[dict]:
    """Return the servers nearest to you, as reported by the CLI."""
    return _run_json(_command(list_servers=True), timeout).get("servers", [])
