n = int(input("Enter number of elements : "))
my_list = list(map(int, input("\nEnter the numbers separated by space: ").strip().split()))[:n]
print("\nList is - ", my_list)


def get_pair_sum(numbers: my_list) -> float:
    """  Implement a function, which returns maximum value of
a1 + a2, a2 + a3, ..., an-1 + an, where a1, ..., aN are numbers in the list """
    new_list = []
    for i in range(len(my_list)):
        if i == 0:
            continue
        else:
            sum_of_elements = numbers[i - 1] + numbers[i]
            new_list.append(sum_of_elements)
    print(new_list)
    max_value = max(new_list)
    print(f'maximum value of the list is: ', max_value)


get_pair_sum(my_list)
