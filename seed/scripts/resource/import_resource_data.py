import csv
import os
import django

from core.models.partner.partner import PartnerModel
from core.models.resource.account import ResourceAccountModel
from core.models.account.account import Persona

from seed.scripts.common.get_account import get_account


def import_resource_accounts(data):
    try:
        print("Adding resource account - {a}".format(a=data['email']))
        account = get_account(data)
        account.persona = Persona.RESOURCE
        account.save()
        partner = PartnerModel.objects.get(email__exact=data['partner_email'])
        ResourceAccountModel(account=account, partner=partner, role=data['role']).save()
    except Exception as exc:
        print("Exception in adding resource account - {a}".format(a=data['email']))
        print(exc)


def main():

    with open('seed/data/resource/resource_accounts.csv', newline='') as csvfile:
        print("Importing resource accounts")
        data = csv.DictReader(csvfile, delimiter=',')
        for row in data:
            try:
                import_resource_accounts(row)
            except:
                print("Error: %s", row)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humancloud.settings')
django.setup()

if __name__ == "__main__":
    main()
else:
    main()
