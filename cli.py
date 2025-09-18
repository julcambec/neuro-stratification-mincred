from pathlib import Path
import json
import typer
import yaml
from datetime import datetime

app = typer.Typer(add_completion=False)


def _read_yaml(path: str) -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f)


@app.command()
def data(config: str = typer.Option(...), outdir: str = typer.Option("data/synthetic")):
    cfg = _read_yaml(config)
    out = Path(outdir)
    out.mkdir(parents=True, exist_ok=True)
    # minimal seeded placeholder file
    meta = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "seed": cfg.get("seed", 42),
        "schema_version": "0.1",
        "rows": 1000,
        "note": "placeholder synthetic file; real generator comes in Day 1 step 2",
    }
    (out / "synth_meta.json").write_text(json.dumps(meta, indent=2))
    typer.echo(f"🧪 Wrote {out/'synth_meta.json'}")


@app.command()
def stratify(
    config: str = typer.Option(...), outdir: str = typer.Option("artifacts/stratify")
):
    Path(outdir).mkdir(parents=True, exist_ok=True)
    (Path(outdir) / "placeholder.txt").write_text("stratify placeholder\n")
    typer.echo("🔍 Stratify placeholder completed.")


@app.command()
def baselines(
    config: str = typer.Option(...), outdir: str = typer.Option("artifacts/baselines")
):
    Path(outdir).mkdir(parents=True, exist_ok=True)
    (Path(outdir) / "placeholder.txt").write_text("baselines placeholder\n")
    typer.echo("📈 Baselines placeholder completed.")


@app.command()
def report(outdir: str = typer.Option("reports")):
    Path(outdir).mkdir(parents=True, exist_ok=True)
    (Path(outdir) / "demo_summary.md").write_text("# Demo summary (placeholder)\n")
    typer.echo("📝 Report placeholder written.")


if __name__ == "__main__":
    app()
