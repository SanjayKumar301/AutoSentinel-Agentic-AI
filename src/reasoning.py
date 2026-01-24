import os
import random
from google import genai
from dotenv import load_dotenv

# 1. Load key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize client (Safe Mode)
client = None
if api_key:
    try:
        client = genai.Client(api_key=api_key)
    except:
        pass

def get_agentic_diagnosis(vehicle_type, sensor_data, anomaly_type):
    """
    Tries AI first. If it fails, falls back to Rule-Based Logic.
    """
    # =====================================================
    # PLAN A: TRY THE REAL AI (Google Gemini)
    # =====================================================
    if client:
        try:
            # THIS PROMPT MUST BE INSIDE THE FUNCTION
            prompt = f"""
            You are a Preventive Maintenance AI. 
            The vehicle is NOT broken yet, but shows early signs of failure.
            
            Situation: {anomaly_type} 
            Current Sensor Readings: RPM={sensor_data['RPM']}, Temp={sensor_data['TEMP']}C.
            
            Task:
            1. Predict what WILL happen if the driver does nothing.
            2. Recommend a PREVENTIVE action to stop it.
            
            Keep it concise (max 2 sentences).
            """
            
            # Try the most stable model
            response = client.models.generate_content(
                model="gemini-1.5-flash", 
                contents=prompt
            )
            return response.text
        except Exception as e:
            # Silently fail and go to Plan B
            pass

    # =====================================================
    # PLAN B: THE "OFFLINE BRAIN" (Safety Net)
    # =====================================================
    if anomaly_type == "RAPID TEMP RISE":
        messages = [
            "Prediction: Coolant boiling imminent. Action: Reduce RPM and turn on heater to dissipate heat.",
            "Prediction: Head gasket stress detected. Action: Stop immediately and check radiator airflow."
        ]
        return random.choice(messages)
        
    elif anomaly_type == "OVERHEATING":
        return "CRITICAL: Engine core temp critical. Action: KILL SWITCH ENGAGED."
        
    else:
        return "Anomaly Detected. Pattern does not match standard faults. Recommendation: Manual Inspection."

# Test it
if __name__ == "__main__":
    print("Testing Reasoning Engine...")
    result = get_agentic_diagnosis("Car", {"RPM": 800, "TEMP": 98, "VIB": 0.5}, "RAPID TEMP RISE")
    print(f"DIAGNOSIS: {result}")