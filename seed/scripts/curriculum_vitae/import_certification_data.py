import csv
import os
import django

from core.models.account.account import AccountModel
from core.models.curriculum_vitae.certification import CertificationModel
from seed.scripts.common.str_to_date import str_to_date


def populate_certification(data, certification: CertificationModel):
    certification.name = data['name']
    certification.issued_date = str_to_date(data['issued_date'])
    certification.expiry_date = str_to_date(data['expiry_date'])


def import_certification(data):
    try:
        print("Adding certification for - {a}".format(a=data['account_email']))
        account = AccountModel.objects.get(email__exact=data['account_email'])
        cv = CertificationModel(curriculum_vitae=account.curriculum_vitae)
        populate_certification(data, cv)
        cv.save()
    except Exception as exc:
        print("Exception in certification for - {a}".format(a=data['account_email']))
        print(exc)


def main():

    with open('seed/data/curriculum_vitae/certification.csv', newline='') as csvfile:
        print("Importing certification")
        data = csv.DictReader(csvfile, delimiter=',')
        for row in data:
            try:
                import_certification(row)
            except:
                print("Error: %s", row)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humancloud.settings')
django.setup()

if __name__ == "__main__":
    main()
else:
    main()
