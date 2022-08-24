import unittest
from task_1_functions_ATM import change_in_one_list, change



class AmountTestCase(unittest.TestCase):

    def test_when_machine_has_given_amount(self):
        amount_of_banknotes = change([1, 2, 5], 7)
        result = change_in_one_list(amount_of_banknotes)
        self.assertEqual(result, [5, 2])

    def test_when_machine_has_not_given_amount(self):
        amount_of_banknotes = change([2, 5], 11)
        result = change_in_one_list(amount_of_banknotes)
        self.assertTrue(result, "Machine has not given amount, please enter amount again")
