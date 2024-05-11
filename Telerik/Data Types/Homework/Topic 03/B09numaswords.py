given_number = int(input())
number_to_check = str(given_number)
number_to_word = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'one hundred',
    200: 'two hundred',
    300: 'three hundred',
    400: 'four hundred',
    500: 'five hundred',
    600: 'six hundred',
    700: 'seven hundred',
    800: 'eight hundred',
    900: 'nine hundred',
}

if len(number_to_check) == 1 or (len(number_to_check) == 2 and given_number <= 20):
    final_answer = number_to_word[given_number]

elif len(number_to_check) == 2 and given_number > 20:
    first_digit = str(number_to_check[0]) + "0"
    second_digit = str(number_to_check[1])
    final_answer = number_to_word[int(first_digit)] + " " + number_to_word[int(second_digit)]

elif len(number_to_check) == 3 and int(number_to_check[1]) != 0 and int(number_to_check[2]) != 0:
    first_digit = str(number_to_check[0]) + "0" + "0"
    third_digit = str(number_to_check[2])
    if int(number_to_check[1]) >= 2:
        second_digit_interim = str(number_to_check[1]) + "0"
        second_digit = number_to_word[int(second_digit_interim)]
        final_answer = number_to_word[int(first_digit)] + " and " + second_digit + " " + number_to_word[int(third_digit)]
    else:
        second_digit_interim = str(number_to_check[1]) + str(number_to_check[2])
        second_digit = number_to_word[int(second_digit_interim)]
        final_answer = number_to_word[int(first_digit)] + " and " + second_digit

elif len(number_to_check) == 3 and int(number_to_check[1]) == 0 and int(number_to_check[2]) != 0:
    first_digit = str(number_to_check[0]) + "0" + "0"
    third_digit = str(number_to_check[2])
    second_digit = ''
    final_answer = number_to_word[int(first_digit)] + " and " + number_to_word[int(third_digit)]

elif len(number_to_check) == 3 and int(number_to_check[1]) == 0 and int(number_to_check[2]) == 0:
    first_digit = str(number_to_check[0]) + "0" + "0"
    final_answer = number_to_word[int(first_digit)]

print(final_answer)