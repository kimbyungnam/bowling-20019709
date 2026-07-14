# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Environment

- Python 3.14.6 via the local venv at `venv/`.
- Activate it before running anything: `venv\Scripts\activate` (PowerShell: `venv\Scripts\Activate.ps1`).
- Dependencies and project metadata are managed via `pyproject.toml`. Keep it in sync as dependencies change.

## Build system

- [Flit](https://flit.pypa.io/) (`flit_core`) is the build backend, configured under `[build-system]` in `pyproject.toml`.
- Package metadata (name, authors, version, description) lives in `[project]`.

## Testing

- `pytest` (with `pytest-cov`) is the test runner, declared under the `test` optional-dependency group in `pyproject.toml`.
- Install test dependencies: `pip install -e .[test]`.
- Run the full suite: `pytest`.
- Run a single test: `pytest path/to/test_file.py::test_name`.

## Getting started

Still to be established:
- The source layout (e.g. a package/module for the solution).
- Any lint/format tooling.

Update this file once those conventions are established so future sessions don't need to rediscover them.
