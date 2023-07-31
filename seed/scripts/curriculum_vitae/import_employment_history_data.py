import csv
import os
import django

from core.models.account.account import AccountModel
from core.models.curriculum_vitae.employment_project import EmploymentHistoryModel
from seed.scripts.common.str_to_bool import str_to_bool
from seed.scripts.common.str_to_date import str_to_date


def populate_employment_history(data, employment_history: EmploymentHistoryModel):
    end_date = None
    if not str_to_bool(data['currently_working']):
        end_date = str_to_date(data['end_date'])

    employment_history.title = data['title']
    employment_history.employment_type = data['employment_type']
    employment_history.company_name = data['company_name']
    employment_history.location = data['location']
    employment_history.start_date = str_to_date(data['start_date'])
    employment_history.end_date = end_date
    employment_history.currently_working = str_to_bool(data['currently_working'])
    employment_history.description = data['description']


def import_employment_history(data):
    try:
        print("Adding employment history for - {a}".format(a=data['account_email']))
        account = AccountModel.objects.get(email__exact=data['account_email'])
        cv = EmploymentHistoryModel(curriculum_vitae=account.curriculum_vitae)
        populate_employment_history(data, cv)
        cv.save()
    except Exception as exc:
        print("Exception in employment history for - {a}".format(a=data['account_email']))
        print(exc)


def main():
    with open('seed/data/curriculum_vitae/employment_history.csv', newline='', encoding="utf8") as csvfile:
        print("Importing employment history")
        data = csv.DictReader(csvfile, delimiter=',')
        for row in data:
            try:
                import_employment_history(row)
            except:
                print("Error: %s", row)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humancloud.settings')
django.setup()

if __name__ == "__main__":
    main()
else:
    main()
