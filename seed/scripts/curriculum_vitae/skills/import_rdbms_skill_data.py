import csv
import os
import django

from core.models.account.account import AccountModel
from core.models.curriculum_vitae.skills.rdbms import RdbmsSkillModel


def populate_rdbms_skill(data, cv: RdbmsSkillModel):
    cv.rdbms_skill_type = data['rdbms_skill_type']
    cv.rating = data['rating']


def import_rdbms_skill(data):
    try:
        print("Adding rdbms skill for - {a}".format(a=data['account_email']))
        account = AccountModel.objects.get(email__exact=data['account_email'])
        cv = RdbmsSkillModel(curriculum_vitae=account.curriculum_vitae)
        populate_rdbms_skill(data, cv)
        cv.save()
    except Exception as exc:
        print("Exception in rdbms skill for - {a}".format(a=data['account_email']))
        print(exc)


def main():

    with open('seed/data/curriculum_vitae/skills/rdbms_skill.csv', newline='') as csvfile:
        print("Importing rdbms skill")
        data = csv.DictReader(csvfile, delimiter=',')
        for row in data:
            try:
                import_rdbms_skill(row)
            except:
                print("Error: %s", row)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humanrdbms.settings')
django.setup()

if __name__ == "__main__":
    main()
else:
    main()
