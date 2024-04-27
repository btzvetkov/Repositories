from datetime import datetime
month_str = input()
day = int(input())
year = 2024

month_dict = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4,
        'May': 5, 'June': 6, 'July': 7, 'August': 8,
        'September': 9, 'October': 10, 'November': 11, 'December': 12
    }

month = month_dict.get(month_str)

date = datetime(year, month, day)

Spring_start = datetime(2024, 3, 20)
Summer_start = datetime(2024, 6, 21)
Autumn_start = datetime(2024, 9, 22)
Winter_start = datetime(2024, 12, 21)


if Summer_start > date >= Spring_start:
    print("Spring")
elif Autumn_start > date >= Summer_start:
    print("Summer")
elif Winter_start > date >= Autumn_start:
    print("Autumn")
else:
    print("Winter")