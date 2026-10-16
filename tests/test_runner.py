import json

import pytest

from speedtest_benchmarker import runner

SAMPLE = {
    "type": "result",
    "timestamp": "2026-10-16T05:01:01Z",
    "ping": {"jitter": 4.5, "latency": 17.4},
    "download": {"bandwidth": 12_500_000, "bytes": 100_000_000},
    "upload": {"bandwidth": 1_250_000, "bytes": 10_000_000},
    "packetLoss": 0,
    "isp": "Example ISP",
    "server": {"id": 123, "name": "Telstra", "location": "Melbourne", "country": "Australia"},
    "result": {"url": "https://www.speedtest.net/result/c/abc"},
}


def test_parse_result_converts_units():
    r = runner.parse_result(SAMPLE, 12.3)
    assert r.download_mbps == 100.0
    assert r.upload_mbps == 10.0
    assert r.download_mb == 100.0
    assert r.server_id == 123
    assert r.duration_s == 12.3


def test_parse_result_missing_field():
    with pytest.raises(runner.SpeedtestError):
        runner.parse_result({"server": {}}, 1)


class FakeProc:
    def __init__(self, stdout="", stderr=""):
        self.stdout, self.stderr = stdout, stderr


def test_run_test(monkeypatch):
    monkeypatch.setattr(runner, "find_cli", lambda: "speedtest")
    monkeypatch.setattr(runner.subprocess, "run", lambda *a, **k: FakeProc(json.dumps(SAMPLE)))
    assert runner.run_test(123).isp == "Example ISP"


def test_cli_error_message(monkeypatch):
    err = json.dumps({"type": "log", "level": "error", "message": "Server not found"})
    monkeypatch.setattr(runner, "find_cli", lambda: "speedtest")
    monkeypatch.setattr(runner.subprocess, "run", lambda *a, **k: FakeProc("", err))
    with pytest.raises(runner.SpeedtestError, match="Server not found"):
        runner.run_test(1)


def test_missing_cli(monkeypatch):
    monkeypatch.setattr(runner.shutil, "which", lambda _: None)
    with pytest.raises(runner.SpeedtestError, match="not found"):
        runner.find_cli()
