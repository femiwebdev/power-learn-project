# COVID Data Analysis & Dashboard

A small exploratory project that loads a COVID-19 CSV, cleans and analyzes the data, and produces visualizations and an interactive dashboard for comparing cases, deaths and vaccinations across countries.

## Objectives

- Load and clean `covid-data.csv` using pandas.
- Inspect and handle missing values, coerce dates, and interpolate numeric series.
- Produce time-series plots (cases, deaths, daily new cases) and summary charts (top countries, heatmap).
- Compute derived metrics: daily new cases (7-day avg) and death rate.
- Build an interactive dashboard (Streamlit) with filters, maps, and downloadable latest-per-country CSV.
- Surface anomalies and guide next steps for deeper analysis.

## Tools & Libraries

- Python 3.8+ (or 3.10/3.11)
- pandas, numpy
- matplotlib, seaborn (optional)
- plotly
- streamlit (for the interactive dashboard)
- pycountry (optional, for ISO code mapping in choropleths)

A requirements file for the Streamlit app is provided as `requirements_streamlit.txt`.

## How to run

1. Open the notebook `report.ipynb` in VS Code (with the Jupyter extension) to explore the step-by-step analysis and visualizations.

2. To run the Streamlit dashboard locally:

```bash
# install dependencies (recommended inside a virtualenv)
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements_streamlit.txt

# run the app (from the project folder containing covid-data.csv)
streamlit run streamlit_app.py
```

3. If you prefer not to install, the notebook provides matplotlib/plotly fallbacks and exports (Plotly figures can be saved to HTML if inline rendering is unavailable).

## Insights & Reflections

- The USA and India show the largest absolute case counts in the dataset; lower totals are observed for Kenya and Nigeria in the provided CSV.
- Rolling averages (7-day) clarify sustained trends vs. reporting spikes; interpolation helps visualization but may mask reporting artifacts.
- Vaccination and ICU/hospitalization fields are optional — when missing, per-capita and capacity analyses are limited.
- For robust choropleths, map non-standard country names to ISO3 codes (pycountry helps but manual mapping may still be required).

## Next steps

- Add a population dataset to compute per-100k metrics.
- Standardize and validate country names and ISO codes for better mapping.
- Add unit tests and a small CI workflow to ensure notebook scripts and the Streamlit app run cleanly.

---

Files of interest:
- `report.ipynb` — analysis notebook
- `streamlit_app.py` — interactive Streamlit dashboard
- `requirements_streamlit.txt` — dependencies for the dashboard
- `covid-data.csv` — input dataset (place in the same folder as above)

