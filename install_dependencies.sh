# Add core dependencies
poetry add pandas numpy scikit-learn

# Add data science dependencies
poetry add matplotlib seaborn jupyterlab

# Add development dependencies
poetry add --group dev black isort mypy pytest

# Add pre-commit
poetry add --group dev pre-commit

# Install git hooks
# Runs all libraries above before every commit
poetry run pre-commit install
