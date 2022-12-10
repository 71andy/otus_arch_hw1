# Unit test HW

## Installing on a local machine

This project requires python 3.10. Python virtual environment should be installed and activated.\
Deps are managed by [pip-tools](https://github.com/jazzband/pip-tools) with requirements stored in [pyproject.toml](https://github.com/jazzband/pip-tools#requirements-from-pyprojecttoml).

Install requirements:

```bash
pip install --upgrade pip pip-tools
make
```

Testing:

```bash
# run lint
make lint

# run unit tests
make test
```
