# python_template


## Install library:

```
pip install -e src/
```

## Run pytests:

To run the tests, make sure that the lib is installed first:
```
pip install -e src/
python -m pytest tests/ -v
```

## Run black:

```
python -m black --check .
```

## Run mypy:

```
python -m mypy src/
```