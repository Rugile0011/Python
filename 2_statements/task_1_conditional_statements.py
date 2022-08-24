my_list = list(range(-5, 5))


def get_number_stats(numbers: my_list) -> dict:
    """Implement a function get_number_stats(numbers: list) -> dict,
    which returns dictionary with these required values """
    max_value = max(my_list)
    min_value = min(my_list)
    average = sum(my_list) / len(my_list)
    in_interval_count = len(my_list)
    positive_count, negative_count = 0, 0
    positive_sum, negative_sum = 0, 0
    for num in my_list:
        if num > 0:
            positive_count += 1
            positive_sum += num
        if num < 0:
            negative_count += 1
            negative_sum += num
    zero_count = my_list.count(0)
    my_dictionary = {'maximum number': max_value, 'minimum number': min_value, 'average number': average,
                     'numbers in interval': in_interval_count,
                     'positive numbers': positive_count, 'negative numbers': negative_count,
                     'how many numbers are equal to 0': zero_count,
                     'sum of positive number': positive_sum, 'sum of negative numbers': negative_sum}
    return my_dictionary


print(get_number_stats(()))
