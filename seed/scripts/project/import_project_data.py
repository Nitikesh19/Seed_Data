import csv
import os

import django

from core.models.client.client import ClientModel
from core.models.project.project import ProjectModel


def populate_project(data, project: ProjectModel):
    project.name = data['name']
    project.display_name = data['display_name']
    project.description = data['description']
    project.status = data['status']


def import_project(data):
    try:
        print("Adding project for - {a}".format(a=data['client_email']))
        client = ClientModel.objects.get(email__exact=data['client_email'])
        project = ProjectModel(client=client)
        populate_project(data, project)
        project.save()
    except Exception as exc:
        print("Exception in project for - {a}".format(a=data['client_email']))
        print(exc)


def main():
    with open('seed/data/project/projects.csv', newline='') as csvfile:
        print("Importing project")
        data = csv.DictReader(csvfile, delimiter=',')
        for row in data:
            try:
                import_project(row)
            except:
                print("Error: %s", row)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humancloud.settings')
django.setup()

if __name__ == "__main__":
    main()
else:
    main()
