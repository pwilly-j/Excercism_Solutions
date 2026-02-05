def is_armstrong_number(number):
    number_string = str(number)
    digits = len(number_string)
    total = 0

    for i in range (0, int(digits)):
        digit_total = int(number_string[i])**int(digits)
        total = total + digit_total
    
    return total == number