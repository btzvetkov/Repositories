a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
    first_number = a
elif b > a and b > c:
    first_number = b
elif c > b and c > a:
    first_number = c

if b < a and b > c:
    second_number = b
elif a > b and a < c:
    second_number = a
elif c < a and c > b:
    second_number = c


if a < b and a < c:
    third_number = a
elif b < a and b < c:
    third_number = b
elif c < b and c < a:
    third_number = c

print(f"{first_number} {second_number} {third_number}")