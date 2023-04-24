# VerBump

### VerBump or Version Bump is a CLI tool that auto-bumps version for your application.

__Currently supports__

- JSON
- TOML

Example - 

- package.json
```json
{
	"version": "0.1.1"
}
```
- pyproject.toml
```toml
[tool.poetry]
version="0.1.0"
```
_Caveat - version attribute should be at top level key/val_

## Install

```bash
pip install verbump
```

## Quick start
```bash
verbump # <command>
verbump major # 1.x.x
verbump minor # x.1.x
verbump patch # x.x.1
```
## Running tests
```bash
poetry install
poetry run tox
```

> Author - [Nikhil Akki](https://nikhilakki.in/about)

> Personal Blog - [nikhilakki.in](https://nikhilakki.in)