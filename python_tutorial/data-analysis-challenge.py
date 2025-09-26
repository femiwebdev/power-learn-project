# Challenge: Perform basic data analysis on a CSV file and generate insights
# Task Requirements: Download or create a CSV file called sales_data.csv with the following columns:
# Date (YYYY-MM-DD)
# Product
# Quantity Sold
# Revenue ($)

# Write a Python script that:
# Load the CSV file using pandas.
# Calculate the total revenue.
# Find the best-selling product (based on Quantity Sold).
# Identify the day with the highest sales.
# Save the results to a new file called sales_summary.txt.

# Print the insights in a user-friendly format.

# Bonus Challenge: Visualize sales trends using matplotlib or seaborn
# Expected Output (sales_summary.txt): Total Revenue: $9,100  Best-Selling Product: Mouse (15 units sold)  Highest Sales Day: 2025-03-01

from pathlib import Path
import pandas as pd
from typing import Optional


def analyze_sales(csv_path: Path, out_path: Path, plot_path: Optional[Path] = None) -> str:
	"""Load sales CSV, compute insights, write summary, and optionally save a plot.

	Returns the single-line summary string written to out_path.
	"""
	df = pd.read_csv(csv_path, parse_dates=["Date"])

	# Ensure expected columns exist
	required = {"Date", "Product", "Quantity Sold", "Revenue ($)"}
	if not required.issubset(df.columns):
		raise ValueError(f"CSV is missing required columns: {required - set(df.columns)}")

	total_revenue = df["Revenue ($)"].sum()

	prod_qty = df.groupby("Product", as_index=False)["Quantity Sold"].sum()
	best = prod_qty.sort_values("Quantity Sold", ascending=False).iloc[0]
	best_product = best["Product"]
	best_qty = int(best["Quantity Sold"]) if not pd.isna(best["Quantity Sold"]) else 0

	day_rev = df.groupby("Date", as_index=False)["Revenue ($)"].sum()
	top_day = day_rev.sort_values("Revenue ($)", ascending=False).iloc[0]["Date"].strftime("%Y-%m-%d")

	summary = (
		f"Total Revenue: ${int(total_revenue):,}  Best-Selling Product: {best_product} ({best_qty} units sold)  "
		f"Highest Sales Day: {top_day}"
	)

	out_path.write_text(summary, encoding="utf-8")

	# Optional plotting (save a small PNG)
	if plot_path is not None:
		try:
			import matplotlib.pyplot as plt

			plot_df = day_rev.sort_values("Date")
			plt.figure(figsize=(6, 3))
			plt.plot(plot_df["Date"], plot_df["Revenue ($)"], marker="o", linewidth=2)
			plt.title("Daily Revenue")
			plt.xlabel("Date")
			plt.ylabel("Revenue ($)")
			plt.grid(alpha=0.3)
			plt.tight_layout()
			plt.savefig(plot_path)
			plt.close()
		except Exception:
			# If plotting fails (no matplotlib), ignore and continue.
			pass

	return summary


if __name__ == "__main__":
	base = Path(__file__).parent
	csv_file = base / "sales_data.csv"
	out_file = base / "sales_summary.txt"
	plot_file = base / "sales_trends.png"

	if not csv_file.exists():
		print(f"Missing {csv_file}. Please create a CSV named 'sales_data.csv' in the same folder.")
	else:
		try:
			result = analyze_sales(csv_file, out_file, plot_file)
			print("Sales analysis complete. Summary:\n", result)
			print(f"Wrote summary to: {out_file}")
			if plot_file.exists():
				print(f"Saved plot to: {plot_file}")
		except Exception as e:
			print("Error during analysis:", e)


