import csv
import os
import django

from core.models.account.account import AccountModel
from core.models.curriculum_vitae.skills.cloud import CloudSkillModel


def populate_cloud_skill(data, cv: CloudSkillModel):
    cv.cloud_skill_type = data['cloud_skill_type']
    cv.rating = data['rating']


def import_cloud_skill(data):
    try:
        print("Adding cloud skill for - {a}".format(a=data['account_email']))
        account = AccountModel.objects.get(email__exact=data['account_email'])
        cv = CloudSkillModel(curriculum_vitae=account.curriculum_vitae)
        populate_cloud_skill(data, cv)
        cv.save()
    except Exception as exc:
        print("Exception in cloud skill for - {a}".format(a=data['account_email']))
        print(exc)


def main():

    with open('seed/data/curriculum_vitae/skills/cloud_skill.csv', newline='') as csvfile:
        print("Importing cloud skill")
        data = csv.DictReader(csvfile, delimiter=',')
        for row in data:
            try:
                import_cloud_skill(row)
            except:
                print("Error: %s", row)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humancloud.settings')
django.setup()

if __name__ == "__main__":
    main()
else:
    main()
