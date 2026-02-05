def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    else:
        return 2 ** (number-1)
    pass

def total():
    total_grains = 0
    for i in range (1,65):
        grains_on_square = square(i)
        total_grains = total_grains + grains_on_square
    return total_grains
    pass
