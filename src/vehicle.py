import random
import time

class VirtualVehicle:
    def __init__(self, vehicle_type="Combustion_Car"):
        self.type = vehicle_type
        self.status = "HEALTHY"
        # We need state variables to handle the "Drift" smoothly
        self.rpm = 2000
        self.temp = 90
        self.vib = 0.3
        
    def generate_data(self):
        """Simulates real-time OBD-II stream"""
        
        # DEFAULT BEHAVIOR (Random small fluctuations)
        if self.status == "HEALTHY":
            self.rpm = random.randint(1500, 2500)
            self.temp = random.uniform(85, 95)
            self.vib = random.uniform(0.1, 0.5)
            
        elif self.status == "OVERHEATING":
            # The 'drift' logic is now handled in main.py, 
            # so here we just return the values set by main.py
            pass 
            
        elif self.status == "BEARING_FAILURE":
            self.rpm = random.randint(2000, 3000)
            self.temp = random.uniform(90, 100)
            self.vib = random.uniform(2.5, 4.0)

        return {"RPM": self.rpm, "TEMP": self.temp, "VIB": self.vib}

    def trigger_fault(self, fault_name):
        self.status = fault_name