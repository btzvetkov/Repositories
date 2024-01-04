line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

horizontal = position[0].upper()
vertical = int(position[1])

if horizontal == "A":
    horizontal_int = int(0)
elif horizontal == 'B':
    horizontal_int = int(1)
elif horizontal == "C":
    horizontal_int = int(2)

if vertical == 1:
    line1[horizontal_int] = "X"
elif vertical == 2:
    line2[horizontal_int] = "X"
elif vertical == 3:
    line3[horizontal_int] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")