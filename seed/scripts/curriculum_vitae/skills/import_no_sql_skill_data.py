import csv
import os
import django

from core.models.account.account import AccountModel
from core.models.curriculum_vitae.skills.no_sql import NoSqlSkillModel


def populate_no_sql_skill(data, cv: NoSqlSkillModel):
    cv.no_sql_skill_type = data['no_sql_skill_type']
    cv.rating = data['rating']


def import_no_sql_skill(data):
    try:
        print("Adding no_sql skill for - {a}".format(a=data['account_email']))
        account = AccountModel.objects.get(email__exact=data['account_email'])
        cv = NoSqlSkillModel(curriculum_vitae=account.curriculum_vitae)
        populate_no_sql_skill(data, cv)
        cv.save()
    except Exception as exc:
        print("Exception in no_sql skill for - {a}".format(a=data['account_email']))
        print(exc)


def main():

    with open('seed/data/curriculum_vitae/skills/no_sql_skill.csv', newline='') as csvfile:
        print("Importing no_sql skill")
        data = csv.DictReader(csvfile, delimiter=',')
        for row in data:
            try:
                import_no_sql_skill(row)
            except:
                print("Error: %s", row)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humanno_sql.settings')
django.setup()

if __name__ == "__main__":
    main()
else:
    main()
