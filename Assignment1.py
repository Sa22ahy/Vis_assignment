# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 01:00:42 2023


"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the data from a CSV file
df = pd.read_csv('D:\dataaa.csv')
df['Date_reported'] = pd.to_datetime(df['Date_reported'])
df['Year'] = df['Date_reported'].dt.year

# Define the list of countries of interest
countries = ['United States of America', 'The United Kingdom', 'Canada']

# Filter the data to include only the specified countries
filtered_df = df[df['Country'].isin(countries)]

# Group the filtered data by year and country, summing the cumulative cases for each group
grouped_df = filtered_df.groupby(['Year', 'Country'])['Cumulative_cases'].sum().reset_index()

# Set up the plot for the first chart
plt.figure(figsize=(10, 6))

# Iterate over the countries and plot a line for each
for country in countries:
    country_data = grouped_df[grouped_df['Country'] == country]
    plt.plot(country_data['Year'], country_data['Cumulative_cases'], label=country)

# Customize the plot for the first chart
plt.title('Sum of Cumulative Cases Over the Years (USA, UK, and Canada)')
plt.xlabel('Year')
plt.ylabel('Cumulative Cases')
plt.ticklabel_format(style='plain', axis='y')
plt.legend()
plt.grid(True)
plt.show()

# Specify the desired year for analysis (for the second chart)
year = 2022  # Replace with the desired year

# Filter the data for the selected year and countries (for the second chart)
filtered_df = df[(df['Country'].isin(countries)) & (df['Year'] == year)]

# Create a bar chart to visualize new cases by country for the specified year (second chart)
plt.figure(figsize=(10, 6))
plt.bar(filtered_df['Country'], filtered_df['New_cases'])
plt.title(f'New Cases by Country in {year}')
plt.xlabel('Country')
plt.ylabel('New Cases')
plt.ticklabel_format(style='plain', axis='y')
plt.show()

# List of countries to be included in the pie chart (for the third chart)
countries = ['United States of America', 'The United Kingdom', 'Canada']  # Replace with the desired countries

# Filter the data to include only the selected countries (for the third chart)
filtered_df = df[df['Country'].isin(countries)]

# Calculate the maximum cumulative cases for each country (for the third chart)
total_cumulative_cases = filtered_df.groupby('Country')['Cumulative_cases'].max()

# Get the labels (country names) and sizes (cumulative case counts) (for the third chart)
labels = total_cumulative_cases.index
sizes = total_cumulative_cases.values

# Create a pie chart to visualize the cumulative cases by country (for the third chart)
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Cumulative Cases by Country (Overall)')
plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.
plt.show()
