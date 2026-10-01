from battery_model import Battery
from bms_logic import BMS


def run_test(test_name, voltage, current, temperature, soc):

    battery = Battery()
    bms = BMS()

    # Set simulated battery values
    battery.voltage = voltage
    battery.current = current
    battery.temperature = temperature
    battery.soc = soc

    status, warnings = bms.check_battery(battery)

    print("\n" + "=" * 45)
    print(test_name)
    print("=" * 45)

    print("Voltage     :", battery.voltage, "V")
    print("Current     :", battery.current, "A")
    print("Temperature :", battery.temperature, "°C")
    print("SOC         :", battery.soc, "%")
    print("BMS Status  :", status)

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(" -", warning)
    else:
        print("No warnings. Battery operating normally.")


# 1. Normal condition
run_test(
    "TEST 1 - NORMAL CONDITION",
    360, 40, 30, 80
)

# 2. Over-temperature
run_test(
    "TEST 2 - OVER TEMPERATURE",
    360, 40, 50, 80
)

# 3. Over-voltage
run_test(
    "TEST 3 - OVER VOLTAGE",
    420, 40, 30, 80
)

# 4. Under-voltage
run_test(
    "TEST 4 - UNDER VOLTAGE",
    280, 40, 30, 80
)

# 5. Over-current
run_test(
    "TEST 5 - OVER CURRENT",
    360, 120, 30, 80
)

# 6. Low SOC
run_test(
    "TEST 6 - LOW SOC",
    360, 40, 30, 5
)