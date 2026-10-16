# Changelog

## 2.0.0

Complete rewrite.

- Installable Python package with a `speedtest-benchmarker` command (`run`, `report`, `servers`).
- Uses the Ookla CLI's JSON output instead of scraping text, so results are reliable.
- Works on Windows, macOS and Linux; no third-party dependencies.
- CSV output now has a header row and consistent units (Mbps, ms, MB).
- Mean/median/min/max summaries and optional percentage-of-plan figures.
- Server lists from the command line, a file, or the N nearest servers.
- Removed the bundled `.exe`/DLLs and the Windows-only extras (`ping_test`, `speedtest-loop`).
- Old v1 result CSVs have no header and are not compatible with `report`.

## 1.x

Original Windows script and PyInstaller build.
