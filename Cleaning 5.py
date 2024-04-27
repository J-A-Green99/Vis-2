import os
import pandas as pd
import shutil

# Input folder containing CSV files
input_folder = "C:/Users/jacka/OneDrive - University of Keele/Visualisation/Cleaned_Questions"

# Output folder for processed files
output_folder = "C:/Users/jacka/OneDrive - University of Keele/Visualisation/Processed_Files"

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate through each CSV file in the input folder
for file_name in os.listdir(input_folder):
    if file_name.endswith(".csv"):
        file_path = os.path.join(input_folder, file_name)
        
        # Read the CSV file
        data = pd.read_csv(file_path)
        
        # Check if any of the specified columns contain non-empty values
        columns_with_data = [col for col in data.columns if data[col].notna().any() and col in ['Age(years)', 'Education', 'Gender', 'Income', 'Race/Ethnicity', 'Total']]
        
        # If at least one column contains data, move the file to a new folder
        if columns_with_data:
            # Create a folder for the column title if it doesn't exist
            column_folder = os.path.join(output_folder, columns_with_data[0])
            if not os.path.exists(column_folder):
                os.makedirs(column_folder)
            
            # Move the file to the column folder
            shutil.move(file_path, os.path.join(column_folder, file_name))
            print(f"File '{file_name}' moved to folder '{columns_with_data[0]}'")
