import os
import pandas as pd

# Read the CSV file
file_path = r'C:/Users/jacka/Downloads/Nutrition__Physical_Activity__and_Obesity_-_Behavioral_Risk_Factor_Surveillance_System_20240328.csv'
data = pd.read_csv(file_path)

# Filter by YearStart: 2020
data = data[data['YearStart'] == 2020]

# Sort by LocationDesc
data = data.sort_values(by='LocationDesc')

# Create a folder to save files if it doesn't exist
folder_path = "C:/Users/jacka/OneDrive - University of Keele/Visualisation/output_files10"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Save each row with a unique StratificationCategory1 value to a different CSV file within the same folder
unique_categories = data['StratificationCategory1'].unique()
for category in unique_categories:
    # Sanitise category name for folder path
    sanitized_category = category.replace("/", "_")  # Replace "/" with "_"
    sanitized_category = sanitized_category.replace("\\", "_")  # Replace "\" with "_"
    file_name = f'{sanitized_category}.csv'
    file_path = os.path.join(folder_path, file_name)
    category_data = data[data['StratificationCategory1'] == category]
    category_data.to_csv(file_path, index=False)
