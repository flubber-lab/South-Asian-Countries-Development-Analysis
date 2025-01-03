## South Asian Countries Development Analysis

## Features of the App:

## Interactive Filters:
**Year:** Select a specific year to analyze.

**Metric:** Choose a metric to visualize on the map and in other charts.

**Countries:** Select specific countries to compare (multi-select).

## Visualizations:

**Scatter Geo Map:** Displays the selected metric for each country on a map. Countries are represented as points, with size and color based on the metric value. Users can hover over points to see specific values.

**Bar Chart:** Compares the selected metric across the selected countries for the chosen year.

**Scatter Plot:** Shows the correlation between the selected metric and GDP per capita.

**Dynamic Updates:**
All visualizations update automatically based on the selected year, metric, and countries.

## How It Works:

**Data Loading:**
The dataset is loaded and cleaned in the load_data() function.
The numeric_columns list is created and returned alongside the DataFrame.
**Filters:**
Users can select a year, metric, and specific countries using the sidebar.
**Visualizations:**
A scatter geo map shows the selected metric for each country.
A bar chart compares the selected metric across the selected countries.
A scatter plot shows the correlation between the selected metric and GDP per capita.

## Example Output:

**Filters:** Users can select a year, metric, and specific countries.

**Visualizations:**

A scatter geo map showing the selected metric for each country.
A bar chart comparing the selected metric across the selected countries.
A scatter plot showing the correlation between the selected metric and GDP per capita.