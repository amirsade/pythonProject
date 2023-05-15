class NormalizeError(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class PhoneNumberError(NormalizeError):

    def __init__(self, phone_number: str, *args: object) -> None:
        self.phone_number = phone_number
        super().__init__(*args)


class EmailError(NormalizeError):

    def __init__(self, email: str, *args: object) -> None:
        self.email = email
        super().__init__(*args)


class PasswordError(NormalizeError):

    def __init__(self, password: str, *args: object) -> None:
        self.password = password
        super().__init__(*args)


class WalletError(NormalizeError):

    def __init__(self, wallet: int, *args: object) -> None:
        self.wallet = wallet
        super().__init__(*args)


def normalize_error_phone(phone_number: str, prefix='+98'):
    phone = phone_number[-10:]
    if len(phone_number) < 10:
        raise PhoneNumberError(phone, 'Number must more of 10 character for credit!')
    elif not phone_number.isnumeric():
        raise PhoneNumberError(phone, 'Phone must be number')
    elif not phone.startswith('9'):
        raise PhoneNumberError(phone, 'Phone must start with 9')
    return prefix + phone


def email_normalize(email: str):
    if '@' not in email:
        raise EmailError(email, 'ERROR! Your email must have "@"! ')
    elif email[-4:] != '.com':
        raise EmailError(email, 'ERROR! Your email not have ".com". ')
    return email


def password_normalize(password: str):
    if len(password) < 8:
        raise PasswordError(password, 'ERROR! Your password must be at least 8 characters and more')
    return password


def wallet_normalize(wallet: int, pay=0):
    if not isinstance(wallet, int):
        raise WalletError(wallet, 'ERROR! invalid literal for int() with base 10')

    if wallet < pay:
        raise WalletError(wallet, 'ERROR! Your assets are less than your payments!')
    return wallet













