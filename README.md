# python-library-template
Template for a Python library that supports data science projects. Setup uses `poetry`.

## Setup

Initialize poetry.
```
poetry install
```

Run Jupyter Lab.
```
poetry run jupyter lab
```

Run tests.
```
poetry run pytest
```


## Next Steps
- Drop datasets or exploratory files into `notebooks/`
- Turn notebook functions into reusable modules in `src/my_data_toolkit/`
- Add more tests in `tests/`
- Use `poetry build` and `poetry publish` when you're ready to share


## Development

Use the following tools to ensure the code is cleaner, safer, and easier to maintain. Add the following tools using the command:
```
poetry add --group dev black isort mypy pytest
```

__`black`__. Code Formatter. Enforces a consistent and clean code style. You don't need to argue about indentation or spacing ever again.
```
poetry run black src/ tests/
```

__`isort`__.  Import Sorter. Automatically sorts imports alphabetically and groups them logically.
```
poetry run isort src/ tests/
```

__`mypy`__. Static type checker. Catches bugs before runtime by checking your type hints.
```
poetry run mypy src/
```

__`pytest`__. Testing framework. Clean, minimal testing tool with great plugin support.
```
poetry run pytest
```
