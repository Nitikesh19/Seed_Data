import csv
import os
import django

from core.models.account.account import AccountModel
from core.models.curriculum_vitae.employment_project import EmploymentProjectModel, EmploymentHistoryModel

from seed.scripts.common.str_to_bool import str_to_bool
from seed.scripts.common.str_to_date import str_to_date


def populate_employment_project(data, employment_project: EmploymentProjectModel):
    end_date = None
    if not str_to_bool(data['currently_working']):
        end_date = str_to_date(data['end_date'])

    employment_project.name = data['name']
    employment_project.start_date = str_to_date(data['start_date'])
    employment_project.end_date = end_date
    employment_project.currently_working = str_to_bool(data['currently_working'])
    employment_project.description = data['description']
    employment_project.roles_and_responsibilities = data['roles_and_responsibilities']
    employment_project.technologies_used = data['technologies_used']


def import_employment_project(data):
    try:
        print("Adding employment project for - {a} and company {b}"
              .format(a=data['account_email'], b=data['employment_company_name']))
        employment = EmploymentHistoryModel.objects.filter(company_name=data['employment_company_name']) \
            .filter(curriculum_vitae__account__email__exact=data['account_email']).first()
        cv = EmploymentProjectModel(employment=employment)
        populate_employment_project(data, cv)
        cv.save()
    except Exception as exc:
        print("Exception in employment project for - {a}".format(a=data['account_email']))
        print(exc)


def main():
    with open('seed/data/curriculum_vitae/employment_project.csv', newline='',encoding="utf8") as csvfile:
        print("Importing employment project")
        data = csv.DictReader(csvfile, delimiter=',')
        for row in data:
            try:
                import_employment_project(row)
            except:
                print("Error: %s", row)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humancloud.settings')
django.setup()

if __name__ == "__main__":
    main()
else:
    main()
