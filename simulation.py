import pandas as pd
from battery_model import Battery
from bms_logic import BMS
import pandas as pd


battery = Battery()
bms = BMS()

simulation_data = []
elapsed_time = 0

# HEV driving cycle
driving_cycle = [
    ("Acceleration", 80, 5),
    ("Cruising", 30, 10),
    ("Regenerative Braking", -40, 5),
    ("Cruising", 30, 10),
    ("Acceleration", 80, 5),
    ("Regenerative Braking", -50, 5),
    ("Cruising", 20, 10)
]

print("=" * 70)
print("HEV BATTERY MANAGEMENT SYSTEM SIMULATION")
print("=" * 70)

for mode, current, duration in driving_cycle:

    time_hours = duration / 60

    # Update battery
    battery.update(current, time_hours)

    # BMS checks battery
    status, warnings = bms.check_battery(battery)

    print("\nDriving Mode :", mode)
    print("Current      :", current, "A")
    print("Duration     :", duration, "minutes")
    print("SOC          :", round(battery.soc, 2), "%")
    print("Voltage      :", battery.voltage, "V")
    print("Temperature  :", round(battery.temperature, 2), "°C")
    print("BMS Status   :", status)

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(" -", warning)
    else:
        print("Warnings     : None")
    # Update elapsed time
    elapsed_time += duration    

    # Store simulation data
    simulation_data.append({
        "Time (min)": elapsed_time,
        "Driving Mode": mode,
        "Current (A)": current,
        "Duration (min)": duration,
        "SOC (%)": round(battery.soc, 2),
        "Voltage (V)": battery.voltage,
        "Temperature (°C)": round(battery.temperature, 2),
        "BMS Status": status,
        "Warnings": ", ".join(warnings) if warnings else "None"
    })


print("\n" + "=" * 70)
print("BMS SIMULATION COMPLETED")
print("=" * 70)

# Save simulation data
df = pd.DataFrame(simulation_data)
df.to_csv("simulation_data.csv", index=False)

print("\nSimulation data saved to simulation_data.csv")