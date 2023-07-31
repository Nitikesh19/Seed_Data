import csv
import os
import django

from core.models.partner.account import PartnerAccountModel
from core.models.account.account import Persona
from core.models.partner.partner import PartnerModel

from seed.scripts.common.get_account import get_account


def import_partner_accounts(data):
    try:
        print("Adding partner account - {a}".format(a=data['email']))
        account = get_account(data)
        account.persona = Persona.PARTNER
        account.save()
        partner = PartnerModel.objects.get(email__exact=data['partner_email'])
        PartnerAccountModel(account=account, partner=partner, role=data['role']).save()
    except Exception as exc:
        print("Exception in adding partner account - {a}".format(a=data['email']))
        print(exc)


def main():

    with open('seed/data/partner/partner_accounts.csv', newline='') as csvfile:
        print("Importing partner accounts")
        data = csv.DictReader(csvfile, delimiter=',')
        for row in data:
            try:
                import_partner_accounts(row)
            except:
                print("Error: %s", row)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humancloud.settings')
django.setup()

if __name__ == "__main__":
    main()
else:
    main()
