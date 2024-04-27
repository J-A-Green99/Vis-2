import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
import seaborn as sns
# Read the shapefile containing the geometries of the United States states

shapefile_path = "C:/Users/jacka/OneDrive - University of Keele/Visualisation/cb_2018_us_state_500k.shp"  # Replace with the path to your shapefile
gdf = gpd.read_file(shapefile_path)

# Check the columns in the GeoDataFrame
print(gdf.columns)



