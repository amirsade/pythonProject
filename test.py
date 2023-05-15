import user_bank
import unittest as test
# import logging as log
# import os
# import json


FILE_TEST = 'Customer_test.json'
dict_test = {'amir195': {'First_name': 'amirSaleh', 'Last_name': 'vafadar', 'Email_person': 'amirsade999@gmail.com',
                         'Password_person': 'Atmosphere', 'Phone_person': '+989360851160', 'Wallet_person': 200000}}


class UserTest(test.TestCase):

    def setUp(self) -> None:
        self.user1 = user_bank.Users('amirSaleh', 'vafadar', 'amir195', 'amirsade999@gmail.com',
                                     'Atmosphere', '+989360851160', 200000)

    def test_register(self):

        self.user1.register_person()
        self.assertEqual(user_bank.dict_of_people, dict_test)

    def test_change_password(self):
        user_name = self.user1.user_name
        new_password = 'ATMOSPHERE'
        dict_test[user_name]['Password_person'] = new_password
        self.user1.register_person()
        self.user1.change_password_person(user_name, new_password)
        self.assertEqual(user_bank.dict_of_people, dict_test)

    def test_change_email(self):
        new_email = 'amirvafadar195@gmail.com'
        dict_test[self.user1.user_name]['Email_person'] = new_email
        self.user1.register_person()
        self.user1.change_email_person(self.user1.user_name, new_email)
        self.assertEqual(user_bank.dict_of_people, dict_test)

    def test_username(self):
        new_username = 'amirSaleh195'
        dict_test[new_username] = dict_test[self.user1.user_name]
        del dict_test[self.user1.user_name]
        self.user1.register_person()
        self.user1.change_user_name(self.user1.user_name, new_username)
        self.assertEqual(user_bank.dict_of_people, dict_test)

    def test_deposit_money(self):
        amount_increase = 100000
        dict_test['amir195']['Wallet_person'] += amount_increase
        self.user1.register_person()
        self.user1.deposit_money('amir195', amount_increase)
        self.assertEqual(user_bank.dict_of_people, dict_test)

    def test_transfer_money(self):
        amount_decrease = 1000
        wallet_person = dict_test['amir195']['Wallet_person']
        if amount_decrease < wallet_person:
            wallet_person -= amount_decrease
            dict_test['amir195']['Wallet_person'] = wallet_person
            self.user1.register_person()
            self.user1.transfer_money('amir195', amount_decrease)
            self.assertEqual(user_bank.dict_of_people, dict_test)


if __name__ == '__main__':
    pass
