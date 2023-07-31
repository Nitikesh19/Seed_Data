import csv
import os
import django

from core.models.account.account import AccountModel
from core.models.curriculum_vitae.domain_expertise import DomainExpertiseModel


def populate_domain_expertise(data, domain_expertise: DomainExpertiseModel):
    domain_expertise.domain = data['domain']
    domain_expertise.exp_in_months = data['exp_in_months']


def import_domain_expertise(data):
    try:
        print("Adding domain expertise for - {a}".format(a=data['account_email']))
        account = AccountModel.objects.get(email__exact=data['account_email'])
        cv = DomainExpertiseModel(curriculum_vitae=account.curriculum_vitae)
        populate_domain_expertise(data, cv)
        cv.save()
    except Exception as exc:
        print("Exception in domain expertise for - {a}".format(a=data['account_email']))
        print(exc)


def main():

    with open('seed/data/curriculum_vitae/domain_expertise.csv', newline='') as csvfile:
        print("Importing domain expertise")
        data = csv.DictReader(csvfile, delimiter=',')
        for row in data:
            try:
                import_domain_expertise(row)
            except:
                print("Error: %s", row)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humancloud.settings')
django.setup()

if __name__ == "__main__":
    main()
else:
    main()
