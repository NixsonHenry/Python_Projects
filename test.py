temperature_readings = [68, 65, 68, 70, 74, 72]

from pathlib import Path
file_path = Path.home() / "temperatures.csv"
with file_path.open(mode="a", encoding="utf-8") as file:
    file.write(str(temperature_readings[0]))
    for temp in temperature_readings[1:]:
        file.write(f",{temp}")

import csv
file_path = Path.home() / "temperatures.csv"
file = file_path.open(mode="w", encoding="utf-8", newline="")

# Create an empty list
daily_temperatures = []
with file_path.open(mode="r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        # Convert row to list of integers
        int_row = [int(value) for value in row]
        # Append the list of integers to daily_temperatures list
        daily_temperatures.append(int_row)

daily_temperatures
[[68, 65, 68, 70, 74, 72], [67, 67, 70, 72, 72, 70],
[68, 70, 74, 76, 74, 73]]