import streamlit as st
import pandas as pd
import os
from collector.collector import run_collection  # Import our function

# --- Page Configuration ---
st.set_page_config(
    page_title="F1 Data Collector",
    page_icon="🏎️",
    layout="centered"
)

# --- App Title and Description ---
st.title("🏎️ F1 Data Collection Utility")
st.markdown("""
This application allows you to download and save Formula 1 race weekend data (Lap Times & Weather) 
for a specific year and Grand Prix. The data is saved locally in a structured format for easy analysis.
""")

# --- User Inputs ---
st.header("1. Select Grand Prix")
year = st.number_input("Enter Year:", min_value=2018, max_value=2024, value=2023)
gp_name = st.text_input("Enter Grand Prix Name:", value="Monaco",
                        help="E.g., 'Monaco', 'Italian Grand Prix', 'Bahrain'")

# --- Run Button and Execution Logic ---
st.header("2. Run the Collector")
if st.button("Start Data Collection"):
    if not gp_name:
        st.error("Please enter a Grand Prix name.")
    else:
        with st.spinner(f"Collecting data for {gp_name} {year}... This may take a few moments."):
            try:
                # Call the collector function
                saved_files = run_collection(year, gp_name)

                st.success("✅ Data collection complete!")
                st.balloons()

                # Display the results
                st.header("3. Results")
                st.write(f"Data saved in: `f1_data_storage/{year}/{gp_name}/`")

                # Show the list of saved files in an expander
                with st.expander("Show saved files and preview data"):
                    for file in saved_files:
                        st.text(file)

                    # Add a button to preview the race lap data
                    race_lap_file = f"f1_data_storage/{year}/{gp_name}/Race_LapData.parquet"
                    if os.path.exists(race_lap_file):
                        st.subheader("Race Lap Data Preview:")
                        df = pd.read_parquet(race_lap_file)
                        st.dataframe(df.head())

            except Exception as e:
                st.error(f"An error occurred during data collection: {e}")