import subprocess
import sys
import pathlib


def test_cli_smoke():
    # Just verifies CLI imports and 'report' target works
    subprocess.run(
        [sys.executable, "cli.py", "report", "--outdir", "reports"], check=True
    )
    assert (pathlib.Path("reports") / "demo_summary.md").exists()
