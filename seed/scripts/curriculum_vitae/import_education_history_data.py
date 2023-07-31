import csv
import os
import django

from core.models.account.account import AccountModel
from core.models.curriculum_vitae.education_history import EducationHistoryModel
from seed.scripts.common.str_to_bool import str_to_bool
from seed.scripts.common.str_to_date import str_to_date


def populate_education_history(data, education_history: EducationHistoryModel):
    education_history.school = data['school']
    education_history.degree = data['degree']
    education_history.field_of_study = data['field_of_study']
    education_history.start_date = str_to_date(data['start_date'])
    education_history.end_date = str_to_date(data['end_date'])
    education_history.pursuing = str_to_bool(data['pursuing'])
    education_history.description = data['description']


def import_education_history(data):
    try:
        print("Adding education history for - {a}".format(a=data['account_email']))
        account = AccountModel.objects.get(email__exact=data['account_email'])
        cv = EducationHistoryModel(curriculum_vitae=account.curriculum_vitae)
        populate_education_history(data, cv)
        cv.save()
    except Exception as exc:
        print("Exception in education history for - {a}".format(a=data['account_email']))
        print(exc)


def main():

    with open('seed/data/curriculum_vitae/education_history.csv', newline='') as csvfile:
        print("Importing education history")
        data = csv.DictReader(csvfile, delimiter=',')
        for row in data:
            try:
                import_education_history(row)
            except:
                print("Error: %s", row)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humancloud.settings')
django.setup()

if __name__ == "__main__":
    main()
else:
    main()
