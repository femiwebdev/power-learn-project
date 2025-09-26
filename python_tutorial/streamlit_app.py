import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Optional helper for ISO codes
try:
    import pycountry
except Exception:
    pycountry = None

st.set_page_config(layout="wide", page_title="COVID Dashboard")

@st.cache_data
def load_data(path: str = "covid-data.csv") -> pd.DataFrame:
    df = pd.read_csv(path)
    # find date column
    date_cols = [c for c in df.columns if 'date' in c.lower()]
    date_col = date_cols[0] if date_cols else df.columns[0]
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df = df.dropna(subset=[date_col])

    # find country column
    country_cols = [c for c in df.columns if c.lower() in ('country','location','country_region','country/region') or 'country' in c.lower() or 'location' in c.lower()]
    country_col = country_cols[0] if country_cols else df.columns[1]

    # numeric cleanup
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    # detect total cases/deaths
    total_cases = next((c for c in df.columns if 'total' in c.lower() and 'case' in c.lower()), None)
    if not total_cases:
        total_cases = next((c for c in df.columns if 'cases' in c.lower()), None)
    total_deaths = next((c for c in df.columns if 'total' in c.lower() and 'death' in c.lower()), None)
    if not total_deaths:
        total_deaths = next((c for c in df.columns if 'deaths' in c.lower()), None)

    # compute daily new cases and death rate
    df = df.sort_values([country_col, date_col])
    if total_cases:
        df['daily_new_cases'] = df.groupby(country_col)[total_cases].diff().fillna(0)
        df['daily_new_cases_7d'] = df.groupby(country_col)['daily_new_cases'].transform(lambda x: x.rolling(7, min_periods=1).mean())
    else:
        df['daily_new_cases'] = np.nan
        df['daily_new_cases_7d'] = np.nan

    if total_cases and total_deaths:
        df['death_rate'] = df[total_deaths] / df[total_cases]
    else:
        df['death_rate'] = np.nan

    # detect hosp/icu columns
    hosp_col = next((c for c in df.columns if 'hosp' in c.lower()), None)
    icu_col = next((c for c in df.columns if 'icu' in c.lower()), None)
    df.attrs['meta'] = {
        'date_col': date_col,
        'country_col': country_col,
        'total_cases_col': total_cases,
        'total_deaths_col': total_deaths,
        'hosp_col': hosp_col,
        'icu_col': icu_col
    }
    return df


def country_to_iso3(name: str) -> str | None:
    if not pycountry:
        return None
    try:
        country = pycountry.countries.search_fuzzy(name)[0]
        return country.alpha_3
    except Exception:
        return None


def prepare_latest(df: pd.DataFrame, country_col: str, date_col: str, total_cases_col: str):
    if total_cases_col:
        latest = df.sort_values(date_col).groupby(country_col, as_index=False).last()
        # attach iso3 if possible
        if 'iso_code' not in latest.columns:
            latest['iso_code'] = latest[country_col].apply(lambda x: country_to_iso3(str(x)) if pycountry else None)
        return latest
    else:
        return df.sort_values(date_col).groupby(country_col, as_index=False).last()


# --- App ---
st.title('COVID-19 interactive dashboard')

# load data
csv_path = st.sidebar.text_input('CSV path', value='covid-data.csv')
with st.spinner('Loading data...'):
    df = load_data(csv_path)
meta = df.attrs.get('meta', {})
date_col = meta.get('date_col')
country_col = meta.get('country_col')
total_cases_col = meta.get('total_cases_col')
total_deaths_col = meta.get('total_deaths_col')
hosp_col = meta.get('hosp_col')
icu_col = meta.get('icu_col')

# sidebar filters
st.sidebar.markdown('## Filters')
all_countries = sorted(df[country_col].dropna().astype(str).unique())
selected_countries = st.sidebar.multiselect('Countries', options=all_countries, default=all_countries[:4])
min_date = df[date_col].min().date()
max_date = df[date_col].max().date()
start_date, end_date = st.sidebar.date_input('Date range', value=(min_date, max_date), min_value=min_date, max_value=max_date)

# filter df
mask = df[country_col].astype(str).isin(selected_countries)
mask = mask & (df[date_col].dt.date >= start_date) & (df[date_col].dt.date <= end_date)
df_filt = df[mask]

# layout: two columns
col1, col2 = st.columns([2,1])

with col1:
    st.subheader('Line charts')
    if total_cases_col:
        fig_cases = px.line(df_filt, x=date_col, y=total_cases_col, color=country_col, title='Total cases over time')
        st.plotly_chart(fig_cases, use_container_width=True)
    else:
        st.info('Total cases column not detected in data')

    if total_deaths_col:
        fig_deaths = px.line(df_filt, x=date_col, y=total_deaths_col, color=country_col, title='Total deaths over time')
        st.plotly_chart(fig_deaths, use_container_width=True)
    else:
        st.info('Total deaths column not detected in data')

    # daily new cases
    if 'daily_new_cases_7d' in df_filt.columns:
        fig_daily = px.line(df_filt, x=date_col, y='daily_new_cases_7d', color=country_col, title='Daily new cases (7-day avg)')
        st.plotly_chart(fig_daily, use_container_width=True)

    # hospitalization/ICU
    if hosp_col or icu_col:
        st.subheader('Hospitalization / ICU')
        if hosp_col and hosp_col in df_filt.columns:
            fig_h = px.line(df_filt, x=date_col, y=hosp_col, color=country_col, title='Hospitalizations over time')
            st.plotly_chart(fig_h, use_container_width=True)
        if icu_col and icu_col in df_filt.columns:
            fig_i = px.line(df_filt, x=date_col, y=icu_col, color=country_col, title='ICU over time')
            st.plotly_chart(fig_i, use_container_width=True)

with col2:
    st.subheader('Latest metrics & maps')
    latest = prepare_latest(df, country_col, date_col, total_cases_col)
    # show table for selected countries
    tbl = latest[latest[country_col].astype(str).isin(selected_countries)]
    st.dataframe(tbl[[country_col, total_cases_col, total_deaths_col]].rename(columns={country_col: 'Country'}).fillna('N/A'))

    # bar chart top countries
    if total_cases_col:
        top = latest.nlargest(10, total_cases_col)
        fig_top = px.bar(top, x=country_col, y=total_cases_col, title='Top 10 countries by total cases')
        st.plotly_chart(fig_top, use_container_width=True)

    # choropleth
    if total_cases_col:
        dfl = latest.copy()
        # ensure iso_code exists
        if 'iso_code' not in dfl.columns:
            dfl['iso_code'] = dfl[country_col].apply(lambda x: country_to_iso3(str(x)) if pycountry else None)
        # if iso codes present, show choropleth
        if dfl['iso_code'].notna().any():
            fig_map = px.choropleth(dfl, locations='iso_code', color=total_cases_col, hover_name=country_col,
                                    color_continuous_scale='Reds', title='Total cases (latest) by country', labels={total_cases_col:'Total cases'})
            st.plotly_chart(fig_map, use_container_width=True)
        else:
            st.info('ISO codes not available for choropleth; install pycountry or add iso_code column to CSV')

st.markdown('---')
st.markdown('Data last updated: **{}**'.format(df[date_col].max().date()))

# expose a download link for latest per-country
@st.cache_data
def latest_csv(df_latest):
    return df_latest.to_csv(index=False).encode('utf-8')

if 'latest' not in globals():
    latest = prepare_latest(df, country_col, date_col, total_cases_col)

if st.button('Download latest per-country CSV'):
    st.download_button('Download CSV', data=latest_csv(latest), file_name='df_latest.csv', mime='text/csv')
