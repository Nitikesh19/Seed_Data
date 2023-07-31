import csv
import os
import django

from core.models.account.account import AccountModel
from core.models.curriculum_vitae.skills.framework import FrameworkSkillModel


def populate_framework_skill(data, cv: FrameworkSkillModel):
    cv.framework_skill_type = data['framework_skill_type']
    cv.rating = data['rating']


def import_framework_skill(data):
    try:
        print("Adding framework skill for - {a}".format(a=data['account_email']))
        account = AccountModel.objects.get(email__exact=data['account_email'])
        cv = FrameworkSkillModel(curriculum_vitae=account.curriculum_vitae)
        populate_framework_skill(data, cv)
        cv.save()
    except Exception as exc:
        print("Exception in framework skill for - {a}".format(a=data['account_email']))
        print(exc)


def main():

    with open('seed/data/curriculum_vitae/skills/framework_skill.csv', newline='') as csvfile:
        print("Importing framework skill")
        data = csv.DictReader(csvfile, delimiter=',')
        for row in data:
            try:
                import_framework_skill(row)
            except:
                print("Error: %s", row)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humanframework.settings')
django.setup()

if __name__ == "__main__":
    main()
else:
    main()
