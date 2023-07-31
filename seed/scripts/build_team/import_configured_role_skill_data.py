import csv
import os
import django

from core.models.build_team.configured_role import ConfiguredRoleModel
from core.models.build_team.configured_role_skill import ConfiguredRoleSkillModel


def populate_configured_role_skill(data, configured_role_skill: ConfiguredRoleSkillModel):
    configured_role_skill.skill = data['skill']


def import_configured_role_skill(data):
    try:
        print("Adding configured role skill - {a}".format(a=data['role']))
        configured_role = ConfiguredRoleModel.objects.get(role__exact=data['role'])
        configured_role_skill = ConfiguredRoleSkillModel(role_id=configured_role)
        populate_configured_role_skill(data, configured_role_skill)
        configured_role_skill.save()

    except Exception as exc:
        print("Exception in adding configured role skill - {a}".format(a=data['role']))
        print(exc)


def main():
    with open('seed/data/build_team/configured_role_skill.csv', newline='') as csvfile:
        print("Importing configured role skill")
        data = csv.DictReader(csvfile, delimiter=',')
        for row in data:
            try:
                import_configured_role_skill(row)
            except:
                print("Error: %s", row)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humancloud.settings')
django.setup()

if __name__ == "__main__":
    main()
else:
    main()
