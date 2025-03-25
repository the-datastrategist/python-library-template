import typer
from my_data_toolkit.preprocessing import clean_column_names
import pandas as pd

app = typer.Typer()

@app.command()
def clean_csv(input: str, output: str):
    """Clean column names in a CSV file."""
    df = pd.read_csv(input)
    df_clean = clean_column_names(df)
    df_clean.to_csv(output, index=False)
    typer.echo(f"Cleaned CSV written to {output}")

if __name__ == "__main__":
    app()
