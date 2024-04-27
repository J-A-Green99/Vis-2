import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv(r"C:/Users/jacka/OneDrive - University of Keele/Visualisation/output_files9/physical_activity_Education.csv")

# Iterate over unique values in the 'Stratification1' column
unique_values = df['Stratification1'].unique()
for value in unique_values:
    # Filter the DataFrame for the current value
    filtered_df = df[df['Stratification1'] == value]
    
    # Pivot the filtered DataFrame to create a heatmap
    pivot_df = filtered_df.pivot(index='LocationDesc', columns='Stratification1', values='Data_Value')
    
    # Create the heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot_df, annot=True, cmap='viridis', fmt=".1f", linewidths=.5)
    plt.title(f"Heatmap for {value}")
    plt.xlabel('Stratification1')
    plt.ylabel('LocationDesc')
    plt.show()
