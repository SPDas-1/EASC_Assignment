sensor_data = {
    "S01": [23.5, 25.2, 27.1, 29.8],
    "S02": [21.4, 24.8, 26.3, 25.7],
    "S03": [30.2, 31.5, 29.9, 32.1]
}

# 1. Calculate average temperature for each sensor
average_temperature = {}

for sensor, temperatures in sensor_data.items():
    average_temperature[sensor] = sum(temperatures) / len(temperatures)

print("Average Temperature of Each Sensor:")
for sensor, average in average_temperature.items():
    print(sensor, ":", round(average, 2), "°C")

# 2. Find the sensor with the highest average temperature
highest_sensor = max(
    average_temperature,
    key=average_temperature.get
)

print("\nSensor with Highest Average Temperature:")
print(highest_sensor, ":", round(average_temperature[highest_sensor], 2), "°C")

# 3. Convert Celsius to Fahrenheit using map() and lambda
fahrenheit_data = {}

for sensor, temperatures in sensor_data.items():
    fahrenheit_data[sensor] = list(
        map(lambda c: (c * 9 / 5) + 32, temperatures)
    )

print("\nTemperatures in Fahrenheit:")
for sensor, temperatures in fahrenheit_data.items():
    print(sensor, ":", [round(t, 2) for t in temperatures])

# 4. Create a set of distinct temperatures greater than 30°C
temperatures_above_30 = {
    temp
    for temperatures in sensor_data.values()
    for temp in temperatures
    if temp > 30
}

print("\nDistinct Temperatures Greater Than 30°C:")
print(temperatures_above_30)

# 5. Sort sensors according to average temperature
sorted_sensors = sorted(
    average_temperature.items(),
    key=lambda x: x[1]
)

print("\nSensors Sorted by Average Temperature:")
for sensor, average in sorted_sensors:
    print(sensor, ":", round(average, 2), "°C")