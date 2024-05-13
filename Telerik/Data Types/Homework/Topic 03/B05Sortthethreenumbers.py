a = int(input())
b = int(input())
c = int(input())

# largest = max(a, b, c)
# smallest = min(a, b, c)
        

if a > b and a > c:
    first_number = a
elif b > a and b > c:
    first_number = b
elif c > b and c > a:
    first_number = c
else:
    first_number = 0

if b < a and b > c:
    second_number = b
elif a > b and a < c:
    second_number = a
elif c < a and c > b:
    second_number = c
else:
    second_number = 0


if a < b and a < c:
    third_number = a
elif b < a and b < c:
    third_number = b
elif c < b and c < a:
    third_number = c
else:
    third_number = 0

print(f"{first_number} {second_number} {third_number}")