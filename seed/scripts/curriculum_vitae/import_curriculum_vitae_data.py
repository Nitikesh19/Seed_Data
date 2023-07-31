import csv
import os
import django

from core.models.account.account import AccountModel
from core.models.curriculum_vitae.curriculum_vitae import CurriculumVitaeModel
from seed.scripts.common.str_to_date import str_to_date


def populate_curriculum_vitae(data, cv: CurriculumVitaeModel):
    cv.cv_type = data['cv_type']
    cv.title = data['title']
    cv.description = data['description']
    cv.summary = data['summary']
    cv.birth_date = str_to_date(data['birth_date'])
    cv.working_since = str_to_date(data['working_since'])


def import_curriculum_vitae(data):
    try:
        print("Adding curriculum vitae for - {a}".format(a=data['account_email']))
        account = AccountModel.objects.get(email__exact=data['account_email'])
        cv = CurriculumVitaeModel(account=account)
        populate_curriculum_vitae(data, cv)
        cv.save()
    except Exception as exc:
        print("Exception in curriculum vitae for - {a}".format(a=data['account_email']))
        print(exc)


def main():

    with open('seed/data/curriculum_vitae/curriculum_vitae.csv', newline='', encoding="utf8") as csvfile:
        print("Importing curriculum vitae")
        data = csv.DictReader(csvfile, delimiter=',')
        for row in data:
            try:
                import_curriculum_vitae(row)
            except:
                print("Error: %s", row)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humancloud.settings')
django.setup()

if __name__ == "__main__":
    main()
else:
    main()

