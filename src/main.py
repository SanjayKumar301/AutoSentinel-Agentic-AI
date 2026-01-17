import time
from colorama import init, Fore, Style
from vehicle import VirtualVehicle
from agent import AgenticAI

# Initialize Colors
init(autoreset=True)

def run_dashboard():
    car = VirtualVehicle()
    agent = AgenticAI()
    
    print(f"{Fore.CYAN}Initializing Agentic Framework... [CONNECTED]")
    time.sleep(1)
    print(f"{Fore.CYAN}Vehicle Profile: {car.type}")
    print("-" * 60)
    print(f"{'TIMESTAMP':<10} | {'RPM':<6} | {'TEMP':<6} | {'VIB':<5} | {'AGENT DIAGNOSIS'}")
    print("-" * 60)

    start_time = time.time()
    try:
        while True:
            elapsed = int(time.time() - start_time)
            data = car.generate_data()
            diagnosis = agent.analyze(data)
            
            print(f"T+{elapsed}s      | {data['RPM']:<6} | {data['TEMP']:.1f}C | {data['VIB']:.2f}G | {diagnosis}")
            
            # Auto-Trigger Faults for the Demo
            if elapsed == 10:
                print(f"\n{Fore.YELLOW}>>> [SCENARIO]: SIMULATING COOLANT LEAK... <<<{Style.RESET_ALL}\n")
                car.trigger_fault("OVERHEATING")
            
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        print("\n[STOP] Simulation ended.")

if __name__ == "__main__":
    run_dashboard()