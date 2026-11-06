import ee
import geopandas as gpd
import pandas as pd
import pyogrio
import shapely
import os
import json
from datetime import datetime


# ============================================================
# CONFIGURATION
# ============================================================

GRID_PATH = "waste_module/data/bengaluru_grid.geojson"

# OpenStreetMap building footprints used for independent built-up coverage.
OSM_FILE = "waste_module/osm_data/southern-zone-260806.osm.pbf"
AREA_CRS = "EPSG:32643"  # UTM zone 43N; suitable for Bengaluru area calculations.

OUTPUT_DIR = "waste_module/satellite/outputs"

OUTPUT_FILE = (
    "waste_module/satellite/outputs/"
    "bengaluru_satellite_features.csv"
)

METADATA_FILE = (
    "waste_module/satellite/outputs/"
    "satellite_metadata.json"
)

SENTINEL_COLLECTION = "COPERNICUS/S2_SR_HARMONIZED"

# ------------------------------------------------------------
# Satellite selection
# ------------------------------------------------------------

# Use a larger temporal window to improve spatial coverage.
COMPOSITE_DAYS = 60

# Keep reasonably clean scenes.
MAX_CLOUD_PERCENT = 50

# Minimum valid pixels required for a grid cell.
MIN_VALID_PIXELS = 5


# ============================================================
# EARTH ENGINE INITIALIZATION
# ============================================================

def initialize_earth_engine():

    print("\nInitializing Google Earth Engine...")

    try:

        ee.Initialize()

        print(
            "Earth Engine initialized successfully."
        )

    except Exception as e:

        print(
            "\nEarth Engine initialization failed."
        )

        print(
            "Run Earth Engine authentication first."
        )

        raise e


# ============================================================
# LOAD GRID
# ============================================================

def load_grid():

    print("\nLoading Bengaluru grid...")

    grid = gpd.read_file(GRID_PATH)

    print(
        "Grid cells:",
        len(grid)
    )

    print(
        "Grid CRS:",
        grid.crs
    )