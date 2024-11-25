### Run

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer): `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
2. Create venv: `uv venv`
3. Install dependencies: `uv pip install -r pyproject.toml`
4. Open Chrome and login
5. Edit configuration variables `main`
6. Run with `uv run main.py`

### Experimental Jupyter Notebook (works only on Linux and MacOS)

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer): `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
2. Create venv: `uv venv`
3. Install dependencies: `uv pip install -r pyproject.toml`
4. Open Chrome and login
5. Run Jupyter: `jupyter lab` or use existing Jupyter
6. Open `notebook.ipynb`
7. Edit configuration variables within first cell
8. Run all cells
