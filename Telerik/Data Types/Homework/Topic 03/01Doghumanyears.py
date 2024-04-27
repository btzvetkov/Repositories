HY = int(input())
DY = 0
interim = 0

if HY <= 2:
    DY = HY * 10
else:
    DY = ((HY - 2) * 4) + 20

print(DY)