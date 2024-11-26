def water_bottle(input_bottles, exchange_value):
    if exchange_value > input_bottles:
        return input_bottles
    else:
        total_extra_bottles = 0
        bottles = input_bottles
        while bottles >= exchange_value:
            extra_bottles = (bottles // exchange_value)
            total_extra_bottles += extra_bottles
            bottles = extra_bottles + (bottles % exchange_value)
        return input_bottles + total_extra_bottles

def water_bottle_1(input_bottles, exchange_value):
    total = input_bottles
    while input_bottles >= exchange_value:
        input_bottles -= exchange_value
        input_bottles += 1
        total += 1
    return total

print(water_bottle_1(15, 4))