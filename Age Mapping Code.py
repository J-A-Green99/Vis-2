import os
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

# Input folder containing CSV files
input_folder = "C:/Users/jacka/OneDrive - University of Keele/Visualisation/Processed_Files/Age(years)"

# Output folder for generated maps
output_folder = "C:/Users/jacka/OneDrive - University of Keele/Visualisation/Choropleth_Maps"

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Function to generate choropleth map for each unique value in a column
def generate_choropleth_maps(csv_file_path, column_name):
    try:
        # Read the CSV file
        data = pd.read_csv(csv_file_path)
        
        # Check if the specified column exists in the dataframe
        if column_name not in data.columns:
            print(f"Column '{column_name}' not found in file '{csv_file_path}'.")
            return
        
        # Get unique values in the specified column
        unique_values = data[column_name].unique()
        
        # Load the GeoJSON file containing state geometries
        geojson_path = "C:/Users/jacka/OneDrive - University of Keele/Visualisation/gz_2010_us_040_00_500k.json"  
        gdf = gpd.read_file(geojson_path)
        
        # Iterate through each unique value and generate a choropleth map
        for value in unique_values:
            subset_data = data[data[column_name] == value]
            
            # Merge data with the geodataframe
            merged = gdf.set_index('NAME').join(subset_data.set_index('LocationDesc'))
            
            # Plot the choropleth map
            fig, ax = plt.subplots(1, 1, figsize=(8, 6))  # Adjust the figsize as needed for zooming in
            merged.plot(column='Data_Value', cmap='OrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
            ax.set_title(f'Choropleth Map Of Obesity Rates By {column_name} = {value}')
            ax.set_xlim(xmin=-130, xmax=-65)  # Adjust the x-axis limits for zooming in
            ax.set_ylim(ymin=20, ymax=50)  # Adjust the y-axis limits for zooming in
            output_filename = f'{os.path.splitext(os.path.basename(csv_file_path))[0]}_{column_name}_{value}_map.png'
            output_path = os.path.join(output_folder, output_filename)
            plt.savefig(output_path)
            plt.close()
            
            print(f"Choropleth map generated for {column_name} = '{value}' and saved as {output_path}")
    except Exception as e:
        print(f"Error occurred while processing file {csv_file_path}: {e}")

# Iterate through each CSV file in the input folder
for file_name in os.listdir(input_folder):
    if file_name.endswith(".csv"):
        file_path = os.path.join(input_folder, file_name)
        
        # Generate choropleth maps for unique values in the specified column
        generate_choropleth_maps(file_path, "Age(years)")
