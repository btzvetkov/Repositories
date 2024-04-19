import math
m = int(input())

if 1 <= m and m <= 100:
    liters_per_km = (4.54 / 1.6) / m
    liters_per_100km = liters_per_km * 100
    result = math.floor(liters_per_100km)
    print(f"{result:.0f} litres per 100 km")
else:
    print()