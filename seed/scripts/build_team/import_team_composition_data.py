
import csv
import os
import django

from core.models.build_team.configured_role import ConfiguredRoleModel
from core.models.build_team.project_request import ProjectRequestModel
from core.models.build_team.team_composition import TeamCompositionModel


def populate_team_composition(data, team_composition: TeamCompositionModel):
    team_composition.role_name = data['role']
    team_composition.required_resource = data['required_resource']
    team_composition.is_full_time = data['is_full_time']
    team_composition.is_role_custom = data['is_role_custom']


def import_team_composition(data):
    try:
        print("Adding team composition - {a}".format(a=data['name']))
        project_request = ProjectRequestModel.objects.get(name__exact=data['name'])
        configured_role = ConfiguredRoleModel.objects.get(role__exact=data['role'])
        team_composition = TeamCompositionModel(project_request=project_request, configured_role=configured_role)
        populate_team_composition(data, team_composition)
        team_composition.save()

    except Exception as exc:
        print("Exception in adding team composition - {a}".format(a=data['role']))
        print(exc)


def main():
    with open('seed/data/build_team/team_composition.csv', newline='') as csvfile:
        print("Importing configured role skill")
        data = csv.DictReader(csvfile, delimiter=',')
        for row in data:
            try:
                import_team_composition(row)
            except:
                print("Error: %s", row)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humancloud.settings')
django.setup()

if __name__ == "__main__":
    main()
else:
    main()
