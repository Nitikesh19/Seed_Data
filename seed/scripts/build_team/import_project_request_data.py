import csv
import os
import django

from core.models.build_team.project_request import ProjectRequestModel


def populate_project_request(data, project_request: ProjectRequestModel):
    project_request.name = data['name']
    project_request.estimated_start_date = data['estimated_start_date']
    project_request.estimated_end_date = data['estimated_end_date']
    project_request.project_description = data['project_description']
    project_request.special_instructions = data['special_instructions']


def import_project_request(data):
    try:
        print("Adding project request - {a}".format(a=data['name']))
        project_request = ProjectRequestModel()
        populate_project_request(data, project_request)
        project_request.save()

    except Exception as exc:
        print("Exception in adding project request - {a}".format(a=data['name']))
        print(exc)


def main():
    with open('seed/data/build_team/project_request.csv', newline='') as csvfile:
        print("Importing project request")
        data = csv.DictReader(csvfile, delimiter=',')
        for row in data:
            try:
                import_project_request(row)
            except:
                print("Error: %s", row)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humancloud.settings')
django.setup()

if __name__ == "__main__":
    main()
else:
    main()
