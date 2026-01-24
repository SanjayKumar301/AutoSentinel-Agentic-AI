import time
from colorama import init, Fore, Back, Style
from vehicle import VirtualVehicle
from agent import AgenticAI
from reasoning import get_agentic_diagnosis

# Initialize Colorama
init(autoreset=True)

def run_dashboard():
    # 1. Initialize
    car = VirtualVehicle()
    agent = AgenticAI()
    
    print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗")
    print(f"{Fore.CYAN}║   PREVENTIVE AGENTIC FRAMEWORK v2.0 (Trend Analysis)       ║")
    print(f"{Fore.CYAN}╚══════════════════════════════════════════════════════════════╝")
    time.sleep(1)
    
    print(f"{Fore.WHITE}System Check: {Fore.GREEN}OK")
    print(f"{Fore.WHITE}Vehicle Profile: {Fore.YELLOW}{car.type}")
    print(f"{Fore.WHITE}Connecting to Reasoning Engine... {Fore.GREEN}CONNECTED")
    time.sleep(1)

    print("-" * 75)
    print(f"{'TIME':<8} | {'RPM':<6} | {'TEMP':<6} | {'VIB':<5} | {'AGENT DIAGNOSIS'}")
    print("-" * 75)

    start_time = time.time()
    
    try:
        while True:
            elapsed = int(time.time() - start_time)
            
            # A. GET DATA
            data = car.generate_data()

            # --- PREVENTIVE SCENARIO INJECTION (The "Drift") ---
            # Between 10s and 25s, we force the temp to rise slowly
            # This simulates a "developing" fault before it breaks
            if elapsed >= 10 and elapsed < 25:
                # Override the random temp with a calculated rising curve
                # 95 -> 117 degrees over 15 seconds
                drift_temp = 95 + (elapsed - 10) * 1.5
                data['TEMP'] = drift_temp
                
                # Visual Indicator of Injection
                if elapsed == 10:
                    print(f"{Fore.MAGENTA}>> [SIMULATION START]: Injecting Slow Coolant Leak Trend...")

            # B. ANALYZE (Now using the "Drifted" data)
            diagnosis_status = agent.analyze(data)
            
            # C. PRINT DASHBOARD
            print(f"T+{elapsed:<5} | {data['RPM']:<6} | {data['TEMP']:.1f}C | {data['VIB']:.2f}G | {diagnosis_status}")
            
            # D. CHECK FOR WARNINGS (Prevention) OR CRITICAL (Protection)
            
            # CASE 1: EARLY WARNING (Yellow) - Prevention
            if "WARNING" in diagnosis_status:
                # Only trigger AI once every 5 seconds to avoid spam
                if elapsed % 5 == 0:
                    print(f"\n{Fore.YELLOW}>>> ⚠️ TREND DETECTED. CONSULTING PREVENTIVE AI...{Style.RESET_ALL}")
                    
                    # Ask AI for "Prevention" advice
                    ai_explanation = get_agentic_diagnosis(car.type, data, "RAPID TEMP RISE")
                    
                    print(f"{Fore.WHITE}{Back.BLUE} 🧠 PREVENTIVE ADVICE: {Style.RESET_ALL}")
                    print(f"{Fore.CYAN}{ai_explanation}\n")
                    time.sleep(2) # Pause for effect

            # CASE 2: CRITICAL FAILURE (Red) - Protection
            elif "CRITICAL" in diagnosis_status:
                print(f"\n{Back.RED}{Fore.WHITE}>>> ⛔ CRITICAL FAILURE. ACTIVATING EMERGENCY PROTOCOL...{Style.RESET_ALL}")
                
                ai_explanation = get_agentic_diagnosis(car.type, data, "OVERHEATING")
                print(f"{Fore.WHITE}{Back.RED} 🧠 EMERGENCY ACTION: {Style.RESET_ALL}")
                print(f"{Fore.RED}{ai_explanation}\n")
                
                print(f"{Fore.WHITE}>> System engaging Kill Switch... (Demo Halted)")
                break # Stop the demo on critical failure

            time.sleep(0.8)
            
    except KeyboardInterrupt:
        print(f"\n\n{Fore.RED}[SYSTEM SHUTDOWN] Demo ended.")

if __name__ == "__main__":
    run_dashboard()













    