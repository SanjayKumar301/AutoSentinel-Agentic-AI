import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

class UniversalScaler:
    def __init__(self):
        self.scaler = StandardScaler()
        
    def fit_and_save(self, df, save_path="../models/scaler.pkl"):
        """
        Learns the 'Normal' distribution of THIS vehicle type.
        """
        print("Scaling data to be Universal (Z-Score Normalization)...")
        self.scaler.fit(df)
        joblib.dump(self.scaler, save_path)
        print(f"Scaler saved to {save_path}")
        
    def transform(self, data):
        return self.scaler.transform(data)

# Usage logic
if __name__ == "__main__":
    # Load the merged data we just created
    df = pd.read_csv("../data/merged_training_data.csv")
    
    scaler = UniversalScaler()
    scaler.fit_and_save(df)
    
    print("Feature Engineering Complete. The AI now sees 'Standard Deviations' instead of raw numbers.")