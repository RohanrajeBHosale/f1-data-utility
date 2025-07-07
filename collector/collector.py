import fastf1 as ff1
import pandas as pd
import os
from pathlib import Path  # Import the modern Path library

# --- THE FIX: Define paths relative to this script's location ---

# Path(os.path.realpath(__file__)) gives the absolute path to THIS script (collector.py)
# .parent gives the directory it's in (the 'collector' folder)
# .parent again gives the parent of that, which is our project's root directory
PROJECT_ROOT = Path(os.path.realpath(__file__)).parent.parent

# Now, build all other paths from this root
DATA_STORE_BASE_DIR = PROJECT_ROOT / "f1_data_storage"


def run_collection(year, grand_prix):
    """
    Main function to orchestrate the data collection for a full race weekend.
    This function can be called by other scripts (like our dashboard).

    Returns a list of paths to the saved files.
    """
    print(f"--- Starting Data Collection for {grand_prix} {year} ---")

    # --- THE FIX: Create and enable the cache using the absolute path ---
    cache_dir = DATA_STORE_BASE_DIR / 'cache'
    os.makedirs(cache_dir, exist_ok=True)  # Ensure the cache directory exists
    ff1.Cache.enable_cache(cache_dir)

    sessions_to_load = ['FP1', 'FP2', 'FP3', 'Q', 'R']
    saved_files = []

    for sess_name in sessions_to_load:
        try:
            session = ff1.get_session(year, grand_prix, sess_name)
            # Use a more targeted load to speed things up
            session.load(telemetry=False, weather=True, messages=False)

            # --- THE FIX: Build session path from the absolute base path ---
            session_path = DATA_STORE_BASE_DIR / str(year) / grand_prix
            os.makedirs(session_path, exist_ok=True)

            laps = session.laps
            if not laps.empty:
                filename = f"{session.name}_LapData.parquet"
                file_path = session_path / filename  # pathlib makes joining paths easy
                laps.to_parquet(file_path, index=False)
                # We return a string version of the path for compatibility
                saved_files.append(str(file_path))
                print(f"  -> Saved Lap Data to {file_path}")

            weather = session.weather_data
            if not weather.empty:
                filename = f"{session.name}_WeatherData.parquet"
                file_path = session_path / filename
                weather.to_parquet(file_path, index=False)
                saved_files.append(str(file_path))
                print(f"  -> Saved Weather Data to {file_path}")

            print(f"--- Finished processing {session.name} ---")

        except Exception as e:
            print(f"Could not load data for session {sess_name}. Error: {e}")

    print("--- Data Collection Finished ---")
    return saved_files


# Make sure your folder is named 'collector' to match the import in app.py
if __name__ == "__main__":
    run_collection(year=2023, grand_prix="Monaco")
