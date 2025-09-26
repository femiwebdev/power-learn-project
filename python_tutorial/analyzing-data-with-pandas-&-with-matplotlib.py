""" This script downloads the Iris dataset (UCI), or uses a
scikit-learn fallback, prints basic diagnostics, and creates four plots. """

from pathlib import Path
from io import StringIO
import sys

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="darkgrid")

URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
COLS = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]


def get_text_from_url(url: str):
    try:
        import requests

        r = requests.get(url, timeout=8)
        r.raise_for_status()
        return r.text
    except Exception:
        return None


def load_iris_from_sklearn():
    from sklearn.datasets import load_iris

    data = load_iris()
    df = pd.DataFrame(data.data, columns=COLS[:-1])
    df["class"] = [f"Iris-{n}" for n in data.target_names[data.target]]
    return df


def main():
    base = Path(__file__).resolve().parent
    raw_file = base / "iris_raw.data"
    csv_file = base / "iris.csv"
    plots_dir = base / "iris_plots"
    plots_dir.mkdir(exist_ok=True)

    text = get_text_from_url(URL)
    if text:
        raw_file.write_text(text, encoding="utf8")
        df = pd.read_csv(StringIO(text), header=None, names=COLS)
    else:
        print("Could not download from UCI — using scikit-learn fallback.")
        df = load_iris_from_sklearn()

    # Basic cleaning: coerce numeric columns and drop rows with missing numeric values
    for c in COLS[:-1]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df = df.dropna().reset_index(drop=True)

    # Quick inspection
    print("\nHead:")
    print(df.head())
    print("\nDtypes:")
    print(df.dtypes)
    print("\nMissing values:")
    print(df.isnull().sum())
    print("\nDescribe:\n", df.describe())

    # Grouping example
    print("\nMean petal_length by class:\n", df.groupby("class")["petal_length"].mean())

    # Save cleaned CSV
    try:
        df.to_csv(csv_file, index=False)
        print(f"Saved cleaned CSV to {csv_file}")
    except Exception as e:
        print("Could not save CSV:", e)

    # Plots
    try:
        # Line: sepal_length over index
        plt.figure(figsize=(9, 4))
        sns.lineplot(x=df.index, y="sepal_length", data=df, marker="o")
        plt.title("Sepal Length (sample index)")
        plt.xlabel("Index")
        plt.ylabel("Sepal Length (cm)")
        plt.tight_layout(); plt.savefig(plots_dir / "line_sepal_length.png"); plt.close()

        # Bar: avg petal_length per class
        plt.figure(figsize=(6, 4))
        avg = df.groupby("class")["petal_length"].mean().sort_values()
        sns.barplot(x=avg.index, y=avg.values, palette="pastel")
        plt.title("Average Petal Length by Class")
        plt.ylabel("Petal Length (cm)")
        plt.tight_layout(); plt.savefig(plots_dir / "bar_avg_petal_length.png"); plt.close()

        # Histogram: sepal_length
        plt.figure(figsize=(6, 4))
        sns.histplot(df["sepal_length"], bins=12, kde=True, color="steelblue")
        plt.title("Distribution of Sepal Length")
        plt.tight_layout(); plt.savefig(plots_dir / "hist_sepal_length.png"); plt.close()

        # Scatter: sepal_length vs petal_length colored by class
        plt.figure(figsize=(6, 5))
        sns.scatterplot(data=df, x="sepal_length", y="petal_length", hue="class", s=70)
        plt.title("Sepal vs Petal Length")
        plt.tight_layout(); plt.savefig(plots_dir / "scatter_sepal_petal.png"); plt.close()

        print(f"Saved plots to {plots_dir}")
    except Exception as e:
        print("Plotting error:", e)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print("Fatal error:", exc)
        sys.exit(1)
