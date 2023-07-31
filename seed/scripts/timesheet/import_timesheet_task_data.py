import csv
import os
import django

from core.models.account.account import AccountModel
from core.models.project.project import ProjectModel
from core.models.project.resource import ProjectResourceModel
from core.models.timesheet import ProjectResourceTimesheetModel
from core.models.timesheet.task import ProjectResourceTimeSheetTaskModel


def populate_timesheet_task_info(data, task: ProjectResourceTimeSheetTaskModel):
    task.task = data['task']
    task.hours_worked = data['hours_worked']
    task.remark = data['remark']


def import_task(data):
    try:
        print("Adding timesheet task for - {a}".format(a=data['account_email']))
        account = AccountModel.objects.get(email__exact=data['account_email'])
        project = ProjectModel.objects.get(name=data['project_name'])
        date = data['date']
        project_resource = ProjectResourceModel.objects.get(account=account, project=project)
        timesheet = ProjectResourceTimesheetModel.objects.get(resource=project_resource, date=date)
        task = ProjectResourceTimeSheetTaskModel(timesheet=timesheet)
        populate_timesheet_task_info(data, task)
        task.save()
    except Exception as exc:
        print("Exception in timesheet task for - {a}".format(a=data['account_email']))
        print(exc)


def main():
    with open('seed/data/timesheet/task.csv', newline='') as csvfile:
        print("Importing task")
        data = csv.DictReader(csvfile, delimiter=',')
        for row in data:
            try:
                import_task(row)
            except:
                print("Error: %s", row)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humancloud.settings')
django.setup()

if __name__ == "__main__":
    main()
else:
    main()
