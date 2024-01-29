target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
final_result = 0
if target <= 1000:
    for n in range (2, target + 1, 2):
        final_result += n
        
print(final_result)