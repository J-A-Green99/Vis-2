import pandas as pd
import os

# Input folder containing CSV files
input_folder = "C:/Users/jacka/OneDrive - University of Keele/Visualisation/Processed_Files/Total"

# Output CSV file
output_file = "C:/Users/jacka/OneDrive - University of Keele/Visualisation/combined_totals.csv"

# Initialize an empty DataFrame to store combined data
combined_df = pd.DataFrame(columns=['LocationDesc'])

# Iterate through each CSV file in the input folder
for file_name in os.listdir(input_folder):
    if file_name.endswith(".csv"):
        file_path = os.path.join(input_folder, file_name)
        data = pd.read_csv(file_path)
        
        # Get the name of the CSV file without the extension
        column_name = file_name[:-4]
        
        # Check if required columns exist in the DataFrame
        if 'Data_Value' in data.columns:
            # Rename the 'Data_Value' column to the filename
            data = data.rename(columns={'Data_Value': column_name})
            
            # Concatenate data based on row index
            combined_df = pd.concat([combined_df, data[['LocationDesc', column_name]]], axis=1)
        else:
            print(f"'Data_Value' column not found in file: {file_name}")

# Sort DataFrame by index
combined_df = combined_df.sort_index(axis=1)

# Drop the first three columns
combined_df = combined_df.iloc[:, 3:]

# Save DataFrame to CSV
combined_df.to_csv(output_file, index=False)
