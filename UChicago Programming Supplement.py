#!/usr/bin/env python
# coding: utf-8

# ## University of Chicago - Programming Supplement
# 
# 

# In[3]:


# Code for MS in Applied Data Science - Aayush


# Q1 Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# File path for the dataset
file_path = r"C:\Users\Aayush\Desktop\BDA\Athletes_winter_games.csv"

# Q2. Read the CSV file into a DataFrame (Ingest data from csv)
df = pd.read_csv(file_path)

#Q3. Manage different data types
#Q6. Wrangling the data using coerse function
df["Age"] = pd.to_numeric(df["Age"], errors='coerce').fillna(0).astype(int)
df["Year"] = pd.to_numeric(df["Year"], errors='coerce').fillna(0).astype(int)

# Q4. Function to analyse data
def display_statistics(data):
    print("\nDescriptive Statistics:\n")
    print(data.describe().round(2))  # Shows statistical summary of numeric columns, rounded to 2 decimals
    print("\nAverage Age of Athletes:\n")
    avg_age = data.groupby("Name")["Age"].mean().round(2)  # Calculates average age for each athlete
    print(avg_age)

# Q5. and Q7. Function to visualise the data in a bar chart
def create_barchart(data, x, y=None, chart_type='matplotlib', agg_func='count', title="Bar Chart",
                    xlabel=None, ylabel=None):
    """
    Creates a bar chart using the specified parameters.
    - Parameters:
      - data: DataFrame to plot.
      - x: Column to use for the x-axis.
      - y: Optional; column to use for the y-axis.
      - chart_type: Type of chart library to use ('matplotlib' in this case).
      - agg_func: Aggregation function applied if 'y' is specified ('count' or other aggregates).
      - title, xlabel, ylabel: Custom labels for the chart, x-axis, and y-axis.

    - If 'chart_type' is 'matplotlib', a bar chart is created with `plot_data`:
      - If 'y' is not specified, counts occurrences of each unique value in `x`.
      - If 'y' is specified, applies the aggregation function `agg_func` to `y` grouped by `x`.
    """
    if chart_type == 'matplotlib':
        # Group data and apply aggregation function
        plot_data = data.groupby(x).size() if y is None else data.groupby(x)[y].agg(agg_func)

        # Plot bar chart
        plot_data.plot(kind='bar', color='skyblue', figsize=(15, 15))
        plt.title(title)
        plt.xlabel(xlabel if xlabel else x)
        plt.ylabel(ylabel if ylabel else f'{agg_func} of {y}' if y else 'Count')
        plt.xticks(rotation=45)  # Rotate x-axis labels for readability
        plt.show()
    else:
        # Notify if an invalid chart type is selected
        print("Invalid chart_type! Please choose 'matplotlib' or 'seaborn'.")

# Display descriptive statistics of the dataset
display_statistics(df)

# Create a bar chart showing the count of athletes by sport
create_barchart(df, x='Sport', chart_type='matplotlib', title='Count of Athletes by Sport')

