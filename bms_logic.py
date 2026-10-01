class BMS:
    def __init__(self):
        self.min_voltage = 300
        self.max_voltage = 400
        self.max_temperature = 45
        self.max_current = 100
        self.min_soc = 10
        self.max_soc = 90

    def check_battery(self, battery):
        warnings = []

        if battery.voltage > self.max_voltage:
            warnings.append("OVER VOLTAGE")

        if battery.voltage < self.min_voltage:
            warnings.append("UNDER VOLTAGE")

        if battery.temperature > self.max_temperature:
            warnings.append("OVER TEMPERATURE")

        if abs(battery.current) > self.max_current:
            warnings.append("OVER CURRENT")

        if battery.soc < self.min_soc:
            warnings.append("LOW SOC")

        if battery.soc > self.max_soc:
            warnings.append("HIGH SOC")

        if len(warnings) == 0:
            return "NORMAL", []

        return "PROTECTION ACTIVE", warnings