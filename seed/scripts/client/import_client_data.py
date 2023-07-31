import csv
import os
import django

from core.models.company.company import CompanyType
from core.models.client.client import ClientModel

from seed.scripts.common.populate_company_info import populate_company_info


def import_client(data):
    try:
        print("Adding client - {a}".format(a=data['company_name']))
        client = ClientModel()
        populate_company_info(data, client)
        client.type = CompanyType.CLIENT
        client.save()
    except Exception as exc:
        print("Exception in adding client - {a}".format(a=data['company_name']))
        print(exc)


def main():

    with open('seed/data/client/clients.csv', newline='') as csvfile:
        print("Importing client")
        data = csv.DictReader(csvfile, delimiter=',')
        for row in data:
            try:
                import_client(row)
            except:
                print("Error: %s", row)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humancloud.settings')
django.setup()

if __name__ == "__main__":
    main()
else:
    main()
