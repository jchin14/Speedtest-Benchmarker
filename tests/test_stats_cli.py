import argparse

import pytest

from speedtest_benchmarker import cli, runner
from speedtest_benchmarker.stats import append_csv, format_summary, read_csv, summarize


def make(server_id=1, down=100.0, up=10.0):
    return runner.Result("2026-01-01T00:00:00Z", server_id, "Name", "City", "AU", "ISP",
                         10.0, 1.0, down, up, 50.0, 5.0, 0.0, 20.0, "url")


def test_csv_roundtrip(tmp_path):
    path = tmp_path / "r.csv"
    append_csv(path, make(1))
    append_csv(path, make(2, down=200))
    assert path.read_text().count("timestamp") == 1  # header written once
    rows = read_csv(path)
    assert [r.server_id for r in rows] == [1, 2]
    assert rows[1].download_mbps == 200


def test_summary_and_plan():
    s = summarize([make(down=100), make(down=300), make(down=200)])
    assert s["download_mbps"]["median"] == 200
    assert s["tests"] == 3
    assert "50.0%" in format_summary(s, (400, 20))  # 200/400 down, 10/20 up


def test_summarize_empty():
    with pytest.raises(ValueError):
        summarize([])


def test_parse_plan():
    assert cli.parse_plan("250/25") == (250, 25)
    with pytest.raises(argparse.ArgumentTypeError):
        cli.parse_plan("fast")


def test_servers_file(tmp_path):
    f = tmp_path / "s.txt"
    f.write_text("# comment\n1 2, 3  # trailing\n\n4\n")
    assert cli.read_servers_file(f) == [1, 2, 3, 4]


def test_run_skips_failures_and_saves(monkeypatch, tmp_path, capsys):
    def fake(server, timeout):
        if server == 2:
            raise runner.SpeedtestError("boom")
        return make(server)

    monkeypatch.setattr(cli, "run_test", fake)
    out = tmp_path / "o.csv"
    code = cli.main(["run", "-s", "1,2,3", "-i", "0", "-o", str(out), "--plan", "100/10"])
    assert code == 0
    assert [r.server_id for r in read_csv(out)] == [1, 3]
    assert "1 failed" in capsys.readouterr().out


def test_report_bad_file(tmp_path):
    assert cli.main(["report", str(tmp_path / "missing.csv")]) == 1
