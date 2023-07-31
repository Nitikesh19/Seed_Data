import csv
import os
import django

from core.models.account.account import AccountModel
from core.models.curriculum_vitae.skills.webserver import WebserverSkillModel


def populate_webserver_skill(data, cv: WebserverSkillModel):
    cv.webserver_skill_type = data['webserver_skill_type']
    cv.rating = data['rating']


def import_webserver_skill(data):
    try:
        print("Adding webserver skill for - {a}".format(a=data['account_email']))
        account = AccountModel.objects.get(email__exact=data['account_email'])
        cv = WebserverSkillModel(curriculum_vitae=account.curriculum_vitae)
        populate_webserver_skill(data, cv)
        cv.save()
    except Exception as exc:
        print("Exception in webserver skill for - {a}".format(a=data['account_email']))
        print(exc)


def main():

    with open('seed/data/curriculum_vitae/skills/webserver_skill.csv', newline='') as csvfile:
        print("Importing webserver skill")
        data = csv.DictReader(csvfile, delimiter=',')
        for row in data:
            try:
                import_webserver_skill(row)
            except:
                print("Error: %s", row)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humanwebserver.settings')
django.setup()

if __name__ == "__main__":
    main()
else:
    main()
