banknotes_or_coins = [2, 5]
amount = round(float(input("Enter amount of money : ")), 2)
print(amount)



def change(banknotes_or_coins, amount, depth=0):
    banknotes_or_coins.sort(reverse=True)
    if depth >= len(banknotes_or_coins):
        return

    banknote = banknotes_or_coins[depth]
    max_possible_number_of_banknotes = int(amount // banknote)

    for number_of_banknotes in reversed(range(max_possible_number_of_banknotes + 1)):
        output = [(number_of_banknotes, banknote)]
        covered_sum = banknote * number_of_banknotes
        remainder = amount - covered_sum

        if remainder == 0:
            return output
        else:
            result_from_deeper_layer = change(banknotes_or_coins, remainder, depth=depth + 1)
            if result_from_deeper_layer:
                return output + result_from_deeper_layer

    return None


new_change_list = change(banknotes_or_coins, amount)


def change_in_one_list(new_change_list):
    """Function, which returns banknotes straight in one list"""
    if not new_change_list:
        return []
    flat_banknotes = []
    for count, banknote in new_change_list:
        for i in range(count):
            flat_banknotes.append(banknote)
    return flat_banknotes


def check_if_change_correct():
    """Check if given amount is correct to user according to the user"""
    flat_banknotes = change_in_one_list(new_change_list)
    sum_of_change = round(sum(flat_banknotes), 2)
    return sum_of_change == amount


print(change_in_one_list(new_change_list))
print(check_if_change_correct())
