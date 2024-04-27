import pandas as pd
import os

# Read the CSV file into a DataFrame
df = pd.read_csv("C:/Users/jacka/Downloads/archive (5)/Nutrition__Physical_Activity__and_Obesity.csv")

# Drop specified columns
columns_to_drop = ['Data_Value_Alt', 'Data_Value_Footnote_Symbol', 'Data_Value_Footnote', 'YearEnd', 'Datasource', 'Total', 'TopicID', 'StratificationID1', 'StratificationCategoryId1']
df = df.drop(columns=columns_to_drop)

# Filter by YearStart: 2020 and Topic: Physical Activity - Behavior
df_filtered = df[(df['YearStart'] == 2020) & (df['Topic'] == 'Physical Activity - Behavior')]

# Order by LocationDesc
df_sorted = df_filtered.sort_values(by='LocationDesc')

# Create a folder to save the CSV files if it doesn't exist
output_folder = 'output_files9'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate over unique values in the 'StratificationCategory1' column
for stratification_value in df_sorted['StratificationCategory1'].unique():
    # Filter the sorted DataFrame for the current stratification_value
    filtered_data = df_sorted[df_sorted['StratificationCategory1'] == stratification_value]
    
    # Construct the file name
    file_name = os.path.join(output_folder, f"physical_activity_{stratification_value}.csv")

    # Ensure that the directory exists before saving the file
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    
    # Save the filtered DataFrame to a new CSV file
    filtered_data.to_csv(file_name, index=False)

    print(f"Saved data for StratificationCategory1 '{stratification_value}' to '{file_name}'")
