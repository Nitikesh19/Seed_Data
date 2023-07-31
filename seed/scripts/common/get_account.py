
from core.models.account.account import AccountModel


def get_account(data):

    account = AccountModel(
        username=data['email'], email=data['email'],
        name=data['name'], phone=data['phone'],
        sex=data['sex'], marital_status=data['marital_status']
    )
    account.set_password(data['pass'])
    account.save()
    return account
