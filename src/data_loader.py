import pandas as pd
import glob
import os

def load_all_data(base_path=".."):
    """
    Recursively finds all CSV files in the data folder and merges them.
    """
    # 1. Find the CSVs (Handling that complex folder structure)
    # This looks for any .csv file inside the 'data' folder
    search_path = os.path.join(base_path, "data", "**", "*.csv")
    csv_files = glob.glob(search_path, recursive=True)
    
    if not csv_files:
        print("❌ No CSV files found! Check your folder structure.")
        return None

    print(f"Found {len(csv_files)} dataset files. Loading...")

    # 2. Loop through and load them
    dfs = []
    for file in csv_files:
        try:
            # The dataset uses ';' as separator sometimes, or ','
            # We try standard read first
            df = pd.read_csv(file)
            # Add a column for the filename (so we know which "trip" this was)
            df['source_file'] = os.path.basename(file)
            dfs.append(df)
        except Exception as e:
            print(f"⚠️ Could not load {file}: {e}")

    # 3. Combine into one massive DataFrame
    full_df = pd.concat(dfs, ignore_index=True)
    
    # 4. Filter for only the columns we actually care about for Health
    # (Based on the Weber dataset description)
    relevant_columns = [
        "Engine RPM", 
        "Engine Coolant Temperature", 
        "Intake Manifold Absolute Pressure",
        "Vehicle Speed Sensor",
        "Intake Air Temperature",
        "Absolute Throttle Position"
    ]
    
    # Check if these columns exist (Data cleaning)
    existing_cols = [c for c in relevant_columns if c in full_df.columns]
    clean_df = full_df[existing_cols].dropna()
    
    print(f"✅ Successfully loaded {len(clean_df)} rows of REAL driving data.")
    return clean_df

if __name__ == "__main__":
    df = load_all_data()
    if df is not None:
        print("\n--- Data Preview ---")
        print(df.head())
        print("\n--- Statistics (The 'Normal' Baseline) ---")
        print(df.describe())
        
        # Save this merged file so we don't have to reload it every time
        df.to_csv("../data/merged_training_data.csv", index=False)
        print("💾 Saved merged data to 'data/merged_training_data.csv'")