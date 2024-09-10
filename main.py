# Necessary libraries
import pandas as pd
import numpy as np

# Load Autoviz
from autoviz import AutoViz_Class

# Load data
df = pd.read_csv("sample-superstore.csv")
df

# Initialize AutoViz class
AV = AutoViz_Class()

# filename = df
# target_variable = "Country Name"
# Select a subset of columns
# selected_columns = ['revenue', 'vote_average', 'popularity', 'budget', 'runtime', 'release_year']
# Filter the DataFrame
# df_reduced = df[selected_columns]

# Visualize data using AutoViz
# dft = AV.AutoViz(
#     "",
#     sep=",",
#     depVar=target_variable,
#     dfte=df,
#     header=0,
#     verbose=2,
#     lowess=False,
#     chart_format="svg",
#     max_rows_analyzed=500,
#     max_cols_analyzed=20,
#     save_plot_dir=None
# )


# Visualize data using AutoViz with a numeric target variable
dft = AV.AutoViz(
    "",
    sep=",",
    depVar="Profit",  # Example of using a numeric column as the target variable
    dfte=df,
    header=0,
    verbose=2,
    lowess=False,
    chart_format="svg",
    max_rows_analyzed=500,
    max_cols_analyzed=20,
    save_plot_dir=None
)