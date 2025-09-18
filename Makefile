# ==== Makefile (Windows + Git Bash) ====
SHELL := bash
PY := ./.venv/Scripts/python.exe
PIP := ./.venv/Scripts/pip.exe

.PHONY: setup data stratify baselines report test fmt lint clean

setup:
	@python -m venv .venv
	@$(PY) -m pip install --upgrade pip
	@$(PY) -m pip install -r requirements.txt
	@./.venv/Scripts/pre-commit.exe install || true
	@echo "✅ Setup complete. Activate with: source .venv/Scripts/activate"

data:
	@$(PY) cli.py data --config configs/demo_synth.yml --outdir data/synthetic

stratify:
	@$(PY) cli.py stratify --config configs/demo_synth.yml --outdir artifacts/stratify

baselines:
	@$(PY) cli.py baselines --config configs/demo_synth.yml --outdir artifacts/baselines

report:
	@$(PY) cli.py report --outdir reports

test:
	@./.venv/Scripts/pytest.exe -q

fmt:
	@./.venv/Scripts/black .
	@./.venv/Scripts/ruff.exe check --fix .

lint:
	@./.venv/Scripts/ruff.exe check .

clean:
	@rm -rf artifacts reports .cache || true
# ==== end of file ====
