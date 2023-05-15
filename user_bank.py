import logging as log
import os
import json

log_format = '%(asctime)s (%(name)s) %(levelname)s: %(message)s'
log.basicConfig(format=log_format, level=log.DEBUG)

# '''
# 1. id person
# 2. l_name person
# 3. f_name person
# 4. u_name person
# 5. email person
# 6. phone_number person
# 7. gender person
# 8. birth_date person
# 9. password person
# 10. change_password person
# 11. change_email person
# 12. change_phone_number person
# 13. wallet person
# 14. Transfer money from wallet
# 15. Deposit money to wallet
# '''
dict_of_people = {}
filename = 'Customers.json'
phone_persons = []


class Users:

    def __init__(self, first_name: str, last_name: str, username: str,
                 email_person: str, password_person: str, phone_person: str, wallet_person: int, *args: object) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = username
        self.email_person = email_person
        self.pass_person = password_person
        self.phone_person = phone_person
        self.wallet_person = wallet_person

        super().__init__(*args)

    def register_person(self):
        if self.phone_person not in phone_persons:
            dict_of_people[f'{self.user_name}'] = {'First_name': self.first_name, 'Last_name': self.last_name,
                                                   'Email_person': self.email_person,
                                                   'Password_person': self.pass_person,
                                                   'Phone_person': self.phone_person,
                                                   'Wallet_person': self.wallet_person}
            phone_persons.append(self.phone_person)
        else:
            log.log(log.ERROR, 'ERROR, you enter phone already exists!')

    @staticmethod
    def change_password_person(user_name: str, new_pass: str):
        if not dict_of_people[user_name]:
            log.log(log.ERROR, 'Your user_name not Exists! you must Sign up!')
        else:
            dict_of_people[user_name]['Password_person'] = new_pass

    @staticmethod
    def change_email_person(user_name: str, new_email: str):
        if not dict_of_people[user_name]:
            log.log(log.ERROR, 'Your user_name not Exists! you must Sign up!')
        else:
            dict_of_people[user_name]['Email_person'] = new_email

    @staticmethod
    def change_user_name(old_user_name: str, new_user_name: str):
        if not dict_of_people[old_user_name]:
            log.log(log.ERROR, 'Your user_name invalid! you must Sign up!')
        else:
            dict_of_people[new_user_name] = dict_of_people[old_user_name]
            del dict_of_people[old_user_name]

    @staticmethod
    def deposit_money(user_name: str, increase_wallet: int):
        wallet = dict_of_people[user_name]['Wallet_person']
        wallet += increase_wallet
        dict_of_people[user_name]['Wallet_person'] = wallet

    @staticmethod
    def transfer_money(user_name: str, pay: int):
        wallet = dict_of_people[user_name]['Wallet_person']
        if wallet > pay:
            wallet -= pay
            dict_of_people[user_name]['Wallet_person'] = wallet
        else:
            log.log(log.ERROR, 'Your wallet is less than your payment!')

    @staticmethod
    def save_in_file():
        if not os.path.isfile(filename):
            with open(filename, 'w') as f:
                json.dump(dict_of_people, f)
        else:
            with open(filename, 'a') as f:
                json.dump(dict_of_people, f)
