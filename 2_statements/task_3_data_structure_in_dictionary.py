from collections import Counter
import re

word = "hello"
my_text = """ Python is a high-level, interpreted, general-purpose programming language. 
Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically-typed 
and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), 
object-oriented and functional programming. It is often described as a 'batteries included' language due to its 
comprehensive standard library.Guido van Rossum began working on Python in the late 1980s as a successor to the 
ABC programming language and first released it in 1991 as Python 0.9.0.[35] Python 2.0 was released in 2000 and 
introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, 
and Unicode support."""

list_of_separate_words = my_text.split(" ")


def find_most_frequent_element(my_text: str) -> list[tuple[str, int]]:
    """Function returns a list of words, which have repeated more than once in the text"""
    c = Counter(list_of_separate_words)
    most_frequent_element_list = []
    for i in c.most_common(len(list_of_separate_words)):
        if i[1] >= 2:
            most_frequent_element_list.append(i)
    return most_frequent_element_list


def find_duplicate_letters(word):
    """Function returns a list of words, which have duplicate letters"""
    double_letters = []
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            double_letters.append(word[i] + word[i + 1])
    return double_letters


double_letters_word = []
for w in list_of_separate_words:
    result = find_duplicate_letters(w)
    if result:
        if w in list_of_separate_words:
            double_letters_word.append(w)
print(double_letters_word)

print(find_most_frequent_element(my_text))
find_most_frequent_element(my_text)
find_duplicate_letters(word)
