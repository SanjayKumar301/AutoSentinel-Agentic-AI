import random

class VirtualVehicle:
    def __init__(self, vehicle_type="Combustion_Car"):
        self.type = vehicle_type
        self.status = "HEALTHY"
        
    def generate_data(self):
        """Simulates real-time OBD-II stream"""
        if self.status == "HEALTHY":
            rpm = random.randint(1500, 2500)
            temp = random.uniform(85, 95)
            vibration = random.uniform(0.1, 0.5)
        elif self.status == "OVERHEATING":
            rpm = random.randint(800, 1200)
            temp = random.uniform(115, 125)
            vibration = random.uniform(0.2, 0.6)
        elif self.status == "BEARING_FAILURE":
            rpm = random.randint(2000, 3000)
            temp = random.uniform(90, 100)
            vibration = random.uniform(2.5, 4.0)

        return {"RPM": rpm, "TEMP": temp, "VIB": vibration}

    def trigger_fault(self, fault_name):
        self.status = fault_name