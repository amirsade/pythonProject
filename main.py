from user_bank import Users, dict_of_people
from handle_error import *
import logging as log

log_format = '%(asctime)s (%(name)s) %(levelname)s: %(message)s'
log.basicConfig(format=log_format, level=log.DEBUG)

manual_string = '''
                    **** THIS IS A LEAST OF PEOPLE IN BANK ****
                                1.Register_person
                                2.Show_least
                                3.Change_password
                                4.Change_email
                                5.Deposit_wallet
                                6.Transfer_wallet
                                7.change_user
                                8.save_persons_in_file

choose your item_number in least: 
'''
choose_user = input(manual_string)
working = False
while not working:
    if choose_user == '1':
        f_name, l_name, u_name, email_p, pass_p, phone_p, wallet_p = input('''Hi please enter identity customers example: 
        amir,vafadar,amir195,amirsade999@gmail.com,password,phone,120000
        now you turn please enter: ''').split(',')
        phone_p = normalize_error_phone(phone_p)
        email_p = email_normalize(email_p)
        pass_p = password_normalize(pass_p)
        wallet_p = int(wallet_p)
        user = Users(f_name, l_name, u_name, email_p, pass_p, phone_p, wallet_p)
        user.register_person()

    elif choose_user == '2':
        print(dict_of_people)

    elif choose_user == '3':
        new_password = input('What do like be new your password: ')
        new_password = password_normalize(new_password)
        user_name = input('Enter your username: ')
        user.change_password_person(user_name, new_password)

    elif choose_user == '4':
        new_email = input('Enter new email: ')
        new_email = email_normalize(new_email)
        user_name = input('Enter your  username: ')
        user.change_email_person(user_name, new_email)

    elif choose_user == '5':
        increase_wallet = int(input('How much do you want to increase your assets?: '))
        user_name = input('Enter your username: ')
        user.deposit_money(user_name, increase_wallet)

    elif choose_user == '6':
        pay = int(input('How much do you want to pay?: '))
        user_name = input('Enter your username: ')
        pay = wallet_normalize(wallet=pay)
        user.transfer_money(user_name, pay)
    elif choose_user == '7':
        old_user, new_user = input('Enter the old and new username respectively(old,new): ').split(',')
        user.change_user_name(old_user, new_user)

    elif choose_user == '8':
        user.save_in_file()
    else:
        log.log(log.ERROR, 'You choose a different character!')
    continue_working = input('If you done enter Q: ').lower()
    if continue_working == 'q':
        working = True
    else:
        choose_user = input(manual_string)
