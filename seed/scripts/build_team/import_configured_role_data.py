import csv
import os
import django

from core.models.build_team.configured_role import ConfiguredRoleModel


def populate_configured_role(data, configured_role: ConfiguredRoleModel):
    configured_role.role = data['role']
    configured_role.experience = data['experience']
    configured_role.operator = data['operator']


def import_configured_role(data):
    try:
        print("Adding configured role - {a}".format(a=data['role']))
        configured_role = ConfiguredRoleModel()
        populate_configured_role(data, configured_role)
        configured_role.save()

    except Exception as exc:
        print("Exception in adding configured role - {a}".format(a=data['role']))
        print(exc)


def main():
    with open('seed/data/build_team/configured_role.csv', newline='') as csvfile:
        print("Importing configured role")
        data = csv.DictReader(csvfile, delimiter=',')
        for row in data:
            try:
                import_configured_role(row)
            except:
                print("Error: %s", row)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humancloud.settings')
django.setup()

if __name__ == "__main__":
    main()
else:
    main()
