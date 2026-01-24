import numpy as np
from collections import deque
from sklearn.ensemble import IsolationForest
from colorama import Fore, Back, Style

class AgenticAI:
    def __init__(self):
        # 1. The Anomaly Detector
        self.model = IsolationForest(contamination=0.1)
        # Train on dummy healthy data
        X_train = np.random.normal(loc=[2000, 90, 0.3], scale=[500, 5, 0.1], size=(100, 3))
        self.model.fit(X_train)
        
        # 2. THE MEMORY BUFFER (For Prevention Trends)
        self.temp_history = deque(maxlen=10)
        self.vib_history = deque(maxlen=10)
        
    def analyze(self, data):
        # Store current data
        self.temp_history.append(data['TEMP'])
        self.vib_history.append(data['VIB'])
        
        # LAYER 1: Critical Checks (Red)
        features = [[data['RPM'], data['TEMP'], data['VIB']]]
        pred = self.model.predict(features)[0]
        
        if pred == -1: 
            if data['TEMP'] > 115: return f"{Back.RED} CRITICAL: OVERHEATING {Style.RESET_ALL}"
            if data['VIB'] > 2.0: return f"{Back.RED} CRITICAL: BEARING FAILURE {Style.RESET_ALL}"

        # LAYER 2: Preventive Checks (Yellow)
        if len(self.temp_history) == 10:
            # Check slope (Current - Oldest)
            temp_change = self.temp_history[-1] - self.temp_history[0]
            
            # If temp rose > 5 degrees in 10 secs, warn user
            if temp_change > 5.0 and data['TEMP'] < 115:
                return f"{Fore.YELLOW}⚠️ WARNING: Rapid Temp Rise (+{temp_change:.1f}C). Predicitng Overheat."

        return f"{Fore.GREEN}SYSTEM OPTIMAL (Stable)"