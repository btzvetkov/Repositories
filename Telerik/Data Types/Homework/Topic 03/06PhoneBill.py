total_messages = int(input())
total_minutes = int(input())
base_bill = 12

if total_messages > 20:
    additional_messages = total_messages - 20
else:
    additional_messages = 0

if total_minutes > 60:
    additional_minutes = total_minutes - 60
else:
    additional_minutes = 0

cost_messages = 0.06
cost_minute = 0.10
tax = 0.2

add_message_cost = additional_messages * cost_messages
add_minutes_cost = additional_minutes * cost_minute

    
add_tax = (add_minutes_cost + add_message_cost) * tax
total_bill = base_bill + add_message_cost + add_minutes_cost + add_tax

print(f"{additional_messages} additional messages for {add_message_cost:.2f} levas")
print(f"{additional_minutes} additional minutes for {add_minutes_cost:.2f} levas")
print(f"{add_tax:.2f} additional taxes")
print(f"{total_bill:.2f} total bill")