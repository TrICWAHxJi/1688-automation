### Run

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer): `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
2. Create venv: `uv venv`
3. Install dependencies: `uv pip install -r pyproject.toml`
4. Edit configuration variables `main.py`
5. Run with `uv run main.py`

### Experimental Jupyter Notebook (works only on Linux and MacOS)

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer): `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
2. Create venv: `uv venv`
3. Install dependencies: `uv pip install -r pyproject.toml`
4. Run Jupyter: `jupyter lab` or use existing Jupyter
5. Open `notebook.ipynb`
6. Edit configuration variables within first cell
7. Run all cells
