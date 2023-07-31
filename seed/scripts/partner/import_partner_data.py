import csv
import os
import django

from core.models.company.company import CompanyType
from core.models.partner.partner import PartnerModel

from seed.scripts.common.populate_company_info import populate_company_info


def import_partner(data):
    try:
        print("Adding partner - {a}".format(a=data['company_name']))
        partner = PartnerModel()
        populate_company_info(data, partner)
        partner.type = CompanyType.PARTNER
        partner.save()
    except Exception as exc:
        print("Exception in adding partner - {a}".format(a=data['company_name']))
        print(exc)


def main():

    with open('seed/data/partner/partners.csv', newline='') as csvfile:
        print("Importing partner")
        data = csv.DictReader(csvfile, delimiter=',')
        for row in data:
            try:
                import_partner(row)
            except:
                print("Error: %s", row)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humancloud.settings')
django.setup()

if __name__ == "__main__":
    main()
else:
    main()
