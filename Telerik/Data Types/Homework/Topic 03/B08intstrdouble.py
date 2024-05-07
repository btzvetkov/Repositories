type_of_string = input()
value_string = input()

if type_of_string == "integer":
    final_value = int(value_string) + 1
    print(final_value)
elif type_of_string == "real":
    final_value = float(value_string) + 1
    print(f"{final_value:.2f}")
elif type_of_string == "text":
    final_value = value_string + "*"
    print(final_value)
