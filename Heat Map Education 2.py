import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
import seaborn as sns

# Read the CSV file into a DataFrame
df = pd.read_csv(r"C:/Users/jacka/OneDrive - University of Keele/Visualisation/output_files9/physical_activity_Education.csv")

# Read the shapefile containing the geometries of the United States states
us_states = gpd.read_file("C:/Users/jacka/OneDrive - University of Keele/Visualisation/cb_2018_us_state_500k.shp")  # Update the path to your shapefile

# Identify the correct column name containing the state names from the us_states GeoDataFrame
# Let's assume the correct column name is 'NAME'
correct_column_name = 'NAME'  

# Merge the GeoDataFrame with the DataFrame using the 'LocationAbbr' column
merged_df = us_states.merge(df, left_on=correct_column_name, right_on='LocationAbbr')

# Iterate over unique values in the 'Stratification1' column
unique_values = df['Stratification1'].unique()
for value in unique_values:
    # Filter the DataFrame for the current value
    filtered_df = merged_df[merged_df['Stratification1'] == value]
    
    # Plot the map
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_title(f"Heatmap for {value}")
    
    # Plot the heatmap using seaborn's heatmap function
    sns.heatmap(data=filtered_df[['Data_Value']].transpose(), ax=ax, cmap='viridis', cbar=True)
    
    # Plot the map of the United States in the background
    us_states.plot(ax=ax, facecolor="none", edgecolor='black')
    
    # Add basemap (contextily)
    ctx.add_basemap(ax, source=ctx.providers.Stamen.TonerLite)
    
    plt.show()
