a = input()
b = input()
larger_value = 0

if a > b:
    larger_value = a
    smaller_value = b
    b = larger_value
    a = smaller_value

print(f"{a} {b}")