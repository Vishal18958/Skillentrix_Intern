class Battery:
    def __init__(self):
        self.capacity = 50
        self.voltage = 360
        self.soc = 80
        self.current = 0
        self.temperature = 30

    def update(self, current, time_hours):
        self.current = current

        soc_change = (current * time_hours / self.capacity) * 100

        self.soc -= soc_change

        self.soc = max(0, min(100, self.soc))

        self.temperature += abs(current) * 0.01

    def get_status(self):
        return {
            "SOC": round(self.soc, 2),
            "Voltage": self.voltage,
            "Current": self.current,
            "Temperature": round(self.temperature, 2)
        }


battery = Battery()

print("Initial Battery Status:")
print(battery.get_status())

battery.update(40, 10 / 60)

print("\nAfter 10 minutes:")
print(battery.get_status())