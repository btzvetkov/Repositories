import math

pi_value = math.pi

radius = float(input())

perimeter = 2 * pi_value * radius

area = pi_value * (radius ** 2)

print(f"{perimeter:.2f}")
print(f"{area:.2f}")