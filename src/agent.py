import numpy as np
from sklearn.ensemble import IsolationForest
from colorama import Fore, Back, Style

class AgenticAI:
    def __init__(self):
        # We pre-train a tiny model on dummy data just for the demo
        self.model = IsolationForest(contamination=0.1)
        X_train = np.random.normal(loc=[2000, 90, 0.3], scale=[500, 5, 0.1], size=(100, 3))
        self.model.fit(X_train)
        
    def analyze(self, data):
        features = [[data['RPM'], data['TEMP'], data['VIB']]]
        pred = self.model.predict(features)[0]
        
        if pred == 1 and data['TEMP'] < 110 and data['VIB'] < 2.0:
            return f"{Fore.GREEN}SYSTEM OPTIMAL"
        else:
            reason = []
            if data['TEMP'] > 110: reason.append("CRITICAL: COOLANT FAILURE")
            if data['VIB'] > 2.0: reason.append("CRITICAL: MOUNTING/BEARING LOOSE")
            if not reason: reason.append("UNKNOWN ANOMALY DETECTED")
            
            return f"{Back.RED}{Fore.WHITE} {' + '.join(reason)} {Style.RESET_ALL}"