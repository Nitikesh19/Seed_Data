import csv
import os
import django

from core.models.account.account import AccountModel
from core.models.curriculum_vitae.skills.language import LanguageSkillModel


def populate_language_skill(data, cv: LanguageSkillModel):
    cv.language_skill_type = data['language_skill_type']
    cv.rating = data['rating']


def import_language_skill(data):
    try:
        print("Adding language skill for - {a}".format(a=data['account_email']))
        account = AccountModel.objects.get(email__exact=data['account_email'])
        cv = LanguageSkillModel(curriculum_vitae=account.curriculum_vitae)
        populate_language_skill(data, cv)
        cv.save()
    except Exception as exc:
        print("Exception in language skill for - {a}".format(a=data['account_email']))
        print(exc)


def main():

    with open('seed/data/curriculum_vitae/skills/language_skill.csv', newline='') as csvfile:
        print("Importing language skill")
        data = csv.DictReader(csvfile, delimiter=',')
        for row in data:
            try:
                import_language_skill(row)
            except:
                print("Error: %s", row)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humanlanguage.settings')
django.setup()

if __name__ == "__main__":
    main()
else:
    main()
