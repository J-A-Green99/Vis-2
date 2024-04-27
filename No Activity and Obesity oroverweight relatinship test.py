import pandas as pd

# Load the CSV file into a DataFrame
file_path = "C:/Users/jacka/OneDrive - University of Keele/Visualisation/combined_totals.csv" # Replace with the actual file path
df = pd.read_csv(file_path)

# Select the columns of interest
selected_columns = [
    'Total_Percent_of_adults_aged_18_years_and_older_who_have_an_overweight_classification',
    'Total_Percent_of_adults_aged_18_years_and_older_who_have_obesity',
    'Total_Percent_of_adults_who_engage_in_no_leisure-time_physical_activity'
]
selected_df = df[selected_columns]

# Calculate the correlation coefficients
correlation_matrix = selected_df.corr()

# Print the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)
