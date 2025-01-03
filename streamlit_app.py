import streamlit as st
import pandas as pd
import plotly.express as px

# Title of the app
st.title("South Asian Dataset Analysis")

# Load the dataset
@st.cache_data  # Cache the data to improve performance
def load_data():
    df = pd.read_csv("South_Asian_dataset.csv")
    # Handle missing values
    df.replace("..", pd.NA, inplace=True)
    df.dropna(inplace=True)
    # Convert columns to numeric
    numeric_columns = [
        'GDP (current US$)', 'GDP growth (annual %)', 'GDP per capita (current US$)',
        'Unemployment, total (% of total labor force) (modeled ILO estimate)', 'Inflation, consumer prices (annual %)',
        'Foreign direct investment, net inflows (% of GDP)', 'Trade (% of GDP)', 'Gini index',
        'Population, total', 'Population growth (annual %)', 'Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)',
        'Life expectancy at birth, total (years)', 'Mortality rate, infant (per 1,000 live births)',
        'Literacy rate, adult total (% of people ages 15 and above)', 'School enrollment, primary (% gross)',
        'Urban population (% of total population)', 'Access to electricity (% of population)',
        'People using at least basic drinking water services (% of population)',
        'People using at least basic sanitation services (% of population)',
        'Carbon dioxide (CO2) emissions excluding LULUCF per capita (t CO2e/capita)',
        'PM2.5 air pollution, mean annual exposure (micrograms per cubic meter)',
        'Renewable energy consumption (% of total final energy consumption)', 'Forest area (% of land area)',
        'Control of Corruption: Percentile Rank', 'Political Stability and Absence of Violence/Terrorism: Estimate',
        'Regulatory Quality: Estimate', 'Rule of Law: Estimate', 'Voice and Accountability: Estimate',
        'Individuals using the Internet (% of population)', 'Research and development expenditure (% of GDP)',
        'High-technology exports (% of manufactured exports)'
    ]
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')
    df.dropna(inplace=True)
    return df, numeric_columns  # Return both the DataFrame and numeric_columns

df, numeric_columns = load_data()  # Load data and get numeric_columns

# Sidebar for filters
st.sidebar.header("Filters")

# Year selection
selected_year = st.sidebar.selectbox("Select Year", sorted(df['Year'].unique()))

# Metric selection
selected_metric = st.sidebar.selectbox(
    "Select Metric",
    options=['GDP (current US$)', 'GDP per capita (current US$)', 'Life expectancy at birth, total (years)',
             'Mortality rate, infant (per 1,000 live births)', 'Literacy rate, adult total (% of people ages 15 and above)',
             'Urban population (% of total population)', 'Access to electricity (% of population)']
)

# Country selection (multi-select)
available_countries = df['Country'].unique()
selected_countries = st.sidebar.multiselect(
    "Select Countries to Compare",
    options=available_countries,
    default=available_countries  # Default to all countries
)

# Filter data based on selected year and countries
filtered_df = df[(df['Year'] == selected_year) & (df['Country'].isin(selected_countries))]

# Display filtered data
st.write(f"Data for the year {selected_year} and selected countries:")
st.write(filtered_df)

# Plot 1: Scatter Geo Map
st.header(f"{selected_metric} by Country in {selected_year}")
fig1 = px.scatter_geo(
    filtered_df,
    locations="Country",  # Column with country names
    locationmode="country names",  # Use country names for mapping
    color=selected_metric,  # Metric to color the points
    hover_name="Country",  # Show country name on hover
    hover_data=[selected_metric],  # Show metric value on hover
    size=selected_metric,  # Size of points based on the metric
    title=f"{selected_metric} by Country in {selected_year}",
    projection="natural earth",  # Map projection
    color_continuous_scale=px.colors.sequential.Plasma  # Color scale
)
st.plotly_chart(fig1)

# Plot 2: Bar Chart for Comparison
st.header(f"Comparison of {selected_metric} Across Selected Countries in {selected_year}")
fig2 = px.bar(
    filtered_df,
    x="Country",
    y=selected_metric,
    title=f"{selected_metric} Across Selected Countries in {selected_year}",
    labels={selected_metric: selected_metric, "Country": "Country"}
)
st.plotly_chart(fig2)

# Plot 3: Scatter Plot for Correlation
st.header(f"Correlation Between {selected_metric} and GDP per Capita in {selected_year}")
fig3 = px.scatter(
    filtered_df,
    x="GDP per capita (current US$)",
    y=selected_metric,
    color="Country",
    hover_name="Country",
    title=f"{selected_metric} vs GDP per Capita in {selected_year}",
    trendline="ols"  # Add a trendline
)
st.plotly_chart(fig3)