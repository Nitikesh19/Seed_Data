import csv
import os
import django

from core.models.account.account import AccountModel
from core.models.project.project import ProjectModel
from core.models.project.resource import ProjectResourceModel
from core.models.timesheet import ProjectResourceTimesheetModel


def populate_timesheet(data, timesheet: ProjectResourceTimesheetModel):
    timesheet.date = data['date']
    timesheet.hours_worked = data['hours_worked']
    timesheet.status = data['status']
    timesheet.remark = data['remark']

def import_timesheet(data):
    try:
        print("Adding timesheet for - {a}".format(a=data['account_email']))
        account = AccountModel.objects.get(email__exact=data['account_email'])
        project = ProjectModel.objects.get(name=data['project_name'])
        project_resource = ProjectResourceModel.objects.get(account=account, project=project)
        timesheet = ProjectResourceTimesheetModel(resource=project_resource)
        populate_timesheet(data, timesheet)
        timesheet.save()

    except Exception as exc:
        print("Exception in timesheet for - {a}".format(a=data['account_email']))
        print(exc)


def main():

    with open('seed/data/timesheet/timesheet.csv', newline='') as csvfile:
        print("Importing timesheet")
        data = csv.DictReader(csvfile, delimiter=',')
        for row in data:
            try:
                import_timesheet(row)
            except:
                print("Error: %s", row)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humancloud.settings')
django.setup()

if __name__ == "__main__":
    main()
else:
    main()