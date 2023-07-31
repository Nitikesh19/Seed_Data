import csv
import os
import django

from core.models.account.account import AccountModel
from core.models.project.project import ProjectModel
from core.models.project.resource import ProjectResourceModel


def populate_project_resource(data, project_resource: ProjectResourceModel):
    project_resource.status = data['status']
    project_resource.start_date = data['start_date']
    project_resource.rate_per_hour = data['rate_per_hour']
def import_project_resource(data):
    try:
        print("Adding project resource for - {a}".format(a=data['account_email']))
        account = AccountModel.objects.get(email__exact=data['account_email'])
        project = ProjectModel.objects.get(name=data['project_name'])
        project_resource = ProjectResourceModel(account=account, project=project)
        populate_project_resource(data, project_resource)
        project_resource.save()
    except Exception as exc:
        print("Exception in project resource for - {a}".format(a=data['account_email']))
        print(exc)

def main():

    with open('seed/data/project/project_resource.csv', newline='') as csvfile:
        print("Importing project resource")
        data = csv.DictReader(csvfile, delimiter=',')
        for row in data:
            try:
                import_project_resource(row)
            except:
                print("Error: %s", row)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humancloud.settings')
django.setup()

if __name__ == "__main__":
    main()
else:
    main()