import geopandas as gpd
import matplotlib.pyplot as plt

# Path to the India shapefile
shapefile_path = "C:/Users/YourUsername/Documents/india_shapefile/INDIA.shp"

# Read the shapefile using GeoPandas
try:
    india_map = gpd.read_file(shapefile_path)

    # Plot the map
    plt.figure(figsize=(10, 10))
    india_map.plot(color="lightblue", edgecolor="black")
    plt.title("Map of India", fontsize=16)
    plt.xlabel("Longitude", fontsize=12)
    plt.ylabel("Latitude", fontsize=12)
    plt.grid(True)
    plt.show()

except FileNotFoundError:
    print("Shapefile not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")
