half_liter_bottles_count = int(input())
one_liter_bottles_count = int(input())

deposit_half_liter = 0.1
deposit_one_liter = 0.25

total_money = (half_liter_bottles_count * deposit_half_liter) + (one_liter_bottles_count * deposit_one_liter)

print(f"{total_money:.2f}")
