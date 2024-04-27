score = int(input())
final_result = 0

if score >= 1 and score <= 3:
    final_result = score * 10
elif score >= 4 and score <= 6:
    final_result = score * 100
elif score >= 7 and score <= 9:
    final_result = score * 1000
elif score < 1 or score > 9:
    final_result = 0
    
if final_result > 0:
    print(final_result)
else:
    print("invalid score")

