# SemVerBump

### SemVerBump or Semantic Version Bump is a CLI tool that auto-bumps version (with auto git tagging and commit) for your application.

__Currently supports__

- JSON

**Example** -

- package.json
```json
{
  "version": "0.1.1"
}
```
_Caveat - version attribute should be in an object and not in a list._


## Supported Runtime
[![pypi](https://img.shields.io/pypi/pyversions/semverbump.svg)](https://pypi.python.org/pypi/semverbump)

- Python 3.9+
## Install

```bash
pip install semverbump
```

## Quick start
```bash
# version file and path defaults to `package.json` and `version` key
semverbump # <command> major | minor | patch
semverbump major # 1.x.x
semverbump minor # x.1.x
semverbump patch # x.x.1
```
## Custom version file and path
```bash
semverbump --version-file app-version.json --version-path project.version minor
# or shorter version
semverbump -f app-version.json -p project.version minor
```

```json
// app-version.json
{
  "project": {
    "name": "SuperApp",
    "version": "1.0.2"
  }
}
```

## Roadmap
- [✅] SemVer support
- [✅] No additional dependencies (Python Standard Libary only)
- [✅] Tested with JSON based configs, it should work with any JSON file if in the format given above.
- [✅] Auto Git commits and Tags
- [🛠️] Add support for more file formats like YAML and TOML
- [❓] Fully compatible with https://semver.org/ spec

## Alternatives (and probably more feature rich) -

- [semver](https://github.com/python-semver/python-semver)
- [verbump](https://github.com/meyt/verbump)
- [bump2version](https://github.com/c4urself/bump2version)


### Contribution -
Feel free to fork it, contributions are welcome!

### License - [MIT](https://github.com/nikhilakki/semverbump/blob/main/LICENSE)
> Author - [Nikhil Akki](https://nikhilakki.in/about)

> Personal Blog - [nikhilakki.in](https://nikhilakki.in)