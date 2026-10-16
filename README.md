# Speedtest Benchmarker

[![CI](https://github.com/jchin14/Speedtest-Benchmarker/actions/workflows/ci.yml/badge.svg)](https://github.com/jchin14/Speedtest-Benchmarker/actions/workflows/ci.yml)

Run [Ookla Speedtest](https://www.speedtest.net/apps/cli) against many servers, log every result to a CSV, and get a summary of how your connection really performs, including how it compares to the plan you pay for.

A single test against your closest server tells you very little. Benchmarking across many servers (domestic and international) shows consistency, peering quality and whether your ISP delivers its advertised speeds.

```
$ speedtest-benchmarker run --nearby 3 --plan 250/25
[1/3] Superloop Australia Pty Ltd (Melbourne, Australia) id=55297  down 235.1  up 24.6 Mbps  ping 15.4 ms
[2/3] Telstra (Windsor, Australia) id=18714  down 228.5  up 24.3 Mbps  ping 16.2 ms
[3/3] Telstra (Melbourne, Australia) id=12491  down 241.9  up 24.7 Mbps  ping 12.8 ms

Saved 3 results to results.csv

3 tests across 3 servers (1.52 GB transferred)

                   mean   median      min      max
  Download       235.17   235.10   228.50   241.90  Mbps
  Upload          24.53    24.60    24.30    24.70  Mbps
  ...
Versus your 250/25 Mbps plan (median):
  Download  94.0%
  Upload    98.4%
```

## Install

You need Python 3.9+ and the official **Ookla Speedtest CLI** (not the `speedtest-cli` pip package) on your `PATH`:

| OS | Install |
| --- | --- |
| macOS | `brew tap teamookla/speedtest && brew install speedtest` |
| Linux | see [speedtest.net/apps/cli](https://www.speedtest.net/apps/cli) |
| Windows | download the zip from the link above and put `speedtest.exe` on your `PATH` |

Then install this tool:

```bash
pipx install git+https://github.com/jchin14/Speedtest-Benchmarker.git
```

Or download the wheel from the [latest release](https://github.com/jchin14/Speedtest-Benchmarker/releases/latest) and `pipx install` it.

## Usage

```bash
speedtest-benchmarker run                     # one test, closest server
speedtest-benchmarker run --nearby 10         # the 10 nearest servers
speedtest-benchmarker run -s 12491,2169       # specific server IDs
speedtest-benchmarker run -f examples/servers-global.txt --plan 250/25
speedtest-benchmarker run --nearby 5 --rounds 4 --interval 30   # repeat over time
speedtest-benchmarker servers                 # list nearby servers and their IDs
speedtest-benchmarker report results.csv --plan 250/25
```

| Option | Description |
| --- | --- |
| `-s, --servers` | Comma separated server IDs |
| `-f, --servers-file` | File of server IDs; `#` comments allowed. [`examples/servers-global.txt`](examples/servers-global.txt) is the 50-server international list from v1 |
| `-n, --nearby` | Test the N nearest servers |
| `-r, --rounds` | Repeat the server list N times |
| `-i, --interval` | Seconds to pause between tests (default 1) |
| `-o, --output` | CSV to append to (default `results.csv`) |
| `--plan DOWN/UP` | Your plan speeds in Mbps, adds percent-of-plan to the summary |
| `--timeout` | Per-test timeout in seconds (default 180) |

Press `Ctrl+C` any time to stop early and see the summary of what completed. Failed or offline servers are skipped and reported.

Each test uses a few hundred MB to over 1 GB of data on fast connections, so a 50 server run can transfer tens of GB. Keep that in mind on metered plans.

### Output

Results append to a CSV with a header row, so you can reopen and extend a run, or load it into a spreadsheet or pandas. Speeds are in Mbps, latency and jitter in ms, data in MB.

`timestamp, server_id, server_name, location, country, isp, latency_ms, jitter_ms, download_mbps, upload_mbps, download_mb, upload_mb, packet_loss, duration_s, result_url`

The first run will accept Ookla's license and GDPR terms on your behalf via the CLI flags `--accept-license --accept-gdpr`. By using this tool you agree to Ookla's [terms](https://www.speedtest.net/about/terms) and [privacy policy](https://www.speedtest.net/about/privacy).

## Upgrading from v1

v1 was a Windows `.exe` that scraped the CLI's text output. v2 is a cross-platform Python package using the CLI's JSON output. The interactive prompts are replaced by command line options, and CSVs now have headers and different columns, so v1 files can't be read by `report`. The old files remain in the git history and the `v1` releases.

## Development

```bash
git clone https://github.com/jchin14/Speedtest-Benchmarker && cd Speedtest-Benchmarker
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest && ruff check .
```

## License

[MIT](LICENSE)
