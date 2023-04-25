# Semsemverbump

### Semsemverbump or Semantic Version Bump is a CLI tool that auto-bumps version for your application.

__Currently supports__

- JSON

Example - 

- package.json
```json
{
	"version": "0.1.1"
}

```

_Caveat - version attribute should be in an object and not in a list._

## Install

```bash
pip install semverbump
```

## Quick start
```bash
semverbump # <command>
semverbump major # 1.x.x
semverbump minor # x.1.x
semverbump patch # x.x.1
```
## Running tests
```bash
poetry install
poetry run tox
```

## Supported Python Runtime
- 3.10 and above
## Roadmap
- [✅] - SemVer support
- [✅] - No additional dependencies (Python Standard Libary only)
- [✅] - Tested with PyProject.toml & Package.json (NodeJS), it should work with any JSON / TOML file if in the format given above.
- [TBD] - Auto Git commits and Tags



> Author - [Nikhil Akki](https://nikhilakki.in/about)

> Personal Blog - [nikhilakki.in](https://nikhilakki.in)