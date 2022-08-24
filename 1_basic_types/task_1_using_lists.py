import math

ranks = [22, 83, 60, 15, 29, 89, 93, 86, 33, 39, 77, 61, 83, 77, 65, 42, 14, 33, 20, 86,
         4, 13, 29, 40, 85, 92, 56, 94, 82, 98, 20, 41, 50, 4, 3, 48, 15, 29, 40, 90]


def average_of_the_list(ranks):
    """Wrote an expression which calculates the average of a list"""
    average = sum(ranks) / len(ranks)
    print("Average of the lists =", round(average, 2))


def list_of_even_elements(ranks):
    """Wrote an expression, which calculates average of even
list elements"""
    new_list = []
    for i in range(len(ranks)):
        if i % 2 == 0:
            new_list.append(ranks[i])
            average_of_even_elements_list = sum(new_list) / len(new_list)
    print("Average of the lists =", average_of_even_elements_list)


def average_of_calculated_elements(ranks):
    """Wrote an expression, which finds the average value of the
provided list, ignoring the 25% smallest and 25% highest list values"""
    ranks.sort()
    new_middle_list = ranks[math.ceil(len(ranks) * 0.25): math.ceil((len(ranks) * 0.75))]
    average = sum(new_middle_list) / len(new_middle_list)
    print("Average of the lists with calculated elements =", average)


average_of_the_list(ranks)
list_of_even_elements(ranks)
average_of_calculated_elements(ranks)
