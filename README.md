# AutoSentinel: Agentic AI for Vehicle Health

**AutoSentinel** is an intelligent IoT framework that acts as a "Digital Mechanic" for vehicles. Unlike traditional OBD-II scanners that only read error codes, AutoSentinel uses an **Agentic AI** approach to:

1.  **Monitor** real-time sensor data (RPM, Temp, Vibration, Voltage).
2.  **Detect** subtle anomalies before they become critical failures (using Machine Learning).
3.  **Reason** about the symptoms to provide specific repair advice.

## Key Features
* **Universal Architecture:** Designed to work across Combustion and Electric Vehicle (EV) profiles.
* **Real-time Diagnostics:** Instant analysis of vehicle health.
* **Fault Injection Simulation:** Built-in capability to simulate critical failures (e.g., Overheating, Bearing Failure) for safety testing.

## Tech Stack
* **Hardware:** ESP32 / ELM327 / IoT Sensors
* **Software:** Python, Scikit-Learn (Isolation Forest), Pandas
* **Interface:** CLI Dashboard / Streamlit