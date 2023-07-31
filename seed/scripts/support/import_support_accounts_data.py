import csv
import os
import django

from core.models.support.account import SupportAccountModel
from core.models.account.account import Persona

from seed.scripts.common.get_account import get_account


def import_support_accounts(data):
    try:
        print("Adding support account - {a}".format(a=data['email']))
        account = get_account(data)
        account.persona = Persona.SUPPORT
        account.save()
        SupportAccountModel(account=account, role=data['role']).save()
    except Exception as exc:
        print("Exception in adding support account - {a}".format(a=data['email']))
        print(exc)


def main():

    with open('seed/data/support/support_accounts.csv', newline='') as csvfile:
        print("Importing support accounts")
        data = csv.DictReader(csvfile, delimiter=',')
        for row in data:
            try:
                import_support_accounts(row)
            except:
                print("Error: %s" % row)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humancloud.settings')
django.setup()

if __name__ == "__main__":
    main()
else:
    main()
