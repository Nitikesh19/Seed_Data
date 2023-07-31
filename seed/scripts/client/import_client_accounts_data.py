import csv
import os
import django

from core.models.client.account import ClientAccountModel
from core.models.account.account import Persona
from core.models.client.client import ClientModel

from seed.scripts.common.get_account import get_account


def import_client_accounts(data):
    try:
        print("Adding client account - {a}".format(a=data['email']))
        account = get_account(data)
        account.persona = Persona.CLIENT
        account.save()
        client = ClientModel.objects.get(email__exact=data['client_email'])
        ClientAccountModel(account=account, client=client, role=data['role']).save()
    except Exception as exc:
        print("Exception in adding client account - {a}".format(a=data['email']))
        print(exc)


def main():

    with open('seed/data/client/client_accounts.csv', newline='') as csvfile:
        print("Importing client accounts")
        data = csv.DictReader(csvfile, delimiter=',')
        for row in data:
            try:
                import_client_accounts(row)
            except:
                print("Error: %s", row)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humancloud.settings')
django.setup()

if __name__ == "__main__":
    main()
else:
    main()
