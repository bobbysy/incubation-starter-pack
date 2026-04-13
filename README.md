# hello-world

A simple Python project with pre-commit hooks for code quality using `uv`, `ruff`, and `pylint`.

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (optional - can use pip instead)

## Setup

### With uv (recommended)

```bash
# Install dependencies
uv sync

# Install pre-commit hooks
uv run pre-commit install
```

### Without uv

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

## Development

Run linters manually:

```bash
# With uv
uv run ruff format
uv run ruff check
uv run pylint hello_world/

# Without uv (in virtual environment)
ruff format
ruff check
pylint hello_world/
```

Run tests:

```bash
# With uv
uv run pytest tests/ -v

# Without uv (in virtual environment)
pytest tests/ -v
```

Run pre-commit hooks on all files:

```bash
uv run pre-commit run --all-files  # With uv
pre-commit run --all-files         # Without uv
```

## Pre-commit Hooks

The following hooks run automatically on each commit:

| Hook | Purpose |
|------|---------|
| `ruff format` | Formats Python code |
| `ruff check` | Checks code style and linting issues |
| `pylint` | Runs pylint for deeper code analysis |

## Project Structure

```
hello-world/
├── pyproject.toml          # Project configuration
├── .pre-commit-config.yaml # Pre-commit hooks configuration
├── README.md               # This file
├── hello_world/
│   ├── __init__.py
│   └── hello_world.py      # Main module
└── tests/
    ├── __init__.py
    ├── conftest.py         # Pytest configuration
    └── test_hello_world.py # Unit tests
```