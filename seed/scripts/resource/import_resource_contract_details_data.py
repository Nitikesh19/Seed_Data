import csv
import os
import django

from core.models.resource.account import ResourceAccountModel
from core.models.resource.contract_detail import ResourceContractDetailModel


def populate_contract_detail(data, contract_detail: ResourceContractDetailModel):
    contract_detail.contract_type = data['contract_type']
    contract_detail.minimum_c2c_term_in_months = float(data['minimum_c2c_term_in_months'])
    contract_detail.expected_rate_per_hour = float(data['expected_rate_per_hour'])


def import_resource_resource_contract_details(data):
    try:
        print("Adding resource resource contract detail - {a}".format(a=data['resource_email']))
        contract_detail = ResourceContractDetailModel()
        populate_contract_detail(data, contract_detail)
        contract_detail.resource_account = ResourceAccountModel.objects.get(account__email__exact=data['resource_email'])
        contract_detail.save()
    except Exception as exc:
        print("Exception in adding resource resource contract detail - {a}".format(a=data['resource_email']))
        print(exc)


def main():

    with open('seed/data/resource/resource_contract_details.csv', newline='') as csvfile:
        print("Importing resource resource contract details")
        data = csv.DictReader(csvfile, delimiter=',')
        for row in data:
            try:
                import_resource_resource_contract_details(row)
            except:
                print("Error: %s", row)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humancloud.settings')
django.setup()

if __name__ == "__main__":
    main()
else:
    main()
