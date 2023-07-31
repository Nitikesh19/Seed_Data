#!/bin/bash
set -x #echo on
rm db.sqlite3
rm -rf ./core/migrations/*.py
touch ./core/migrations/__init__.py
python3 ./manage.py makemigrations
if [ $? -ne 0 ]; then
  exit 1
fi
python3 ./manage.py migrate
python3 ./manage.py shell < ./seed/scripts/import_data.py
python3 ./manage.py shell < ./seed/scripts/client/import_client_data.py
python3 ./manage.py shell < ./seed/scripts/client/import_client_accounts_data.py
python3 ./manage.py shell < ./seed/scripts/partner/import_partner_data.py
python3 ./manage.py shell < ./seed/scripts/partner/import_partner_accounts_data.py
python3 ./manage.py shell < ./seed/scripts/resource/import_resource_data.py
python3 ./manage.py shell < ./seed/scripts/resource/import_resource_contract_details_data.py
python3 ./manage.py shell < ./seed/scripts/support/import_support_accounts_data.py
python3 ./manage.py shell < ./seed/scripts/curriculum_vitae/import_curriculum_vitae_data.py
python3 ./manage.py shell < ./seed/scripts/curriculum_vitae/import_domain_expertise_data.py
python3 ./manage.py shell < ./seed/scripts/curriculum_vitae/import_certification_data.py
python3 ./manage.py shell < ./seed/scripts/curriculum_vitae/import_education_history_data.py
python3 ./manage.py shell < ./seed/scripts/curriculum_vitae/import_employment_history_data.py
python3 ./manage.py shell < ./seed/scripts/curriculum_vitae/import_employment_project_data.py
python3 ./manage.py shell < ./seed/scripts/curriculum_vitae/skills/import_cloud_skill_data.py
python3 ./manage.py shell < ./seed/scripts/curriculum_vitae/skills/import_framework_skill_data.py
python3 ./manage.py shell < ./seed/scripts/curriculum_vitae/skills/import_language_skill_data.py
python3 ./manage.py shell < ./seed/scripts/curriculum_vitae/skills/import_no_sql_skill_data.py
python3 ./manage.py shell < ./seed/scripts/curriculum_vitae/skills/import_rdbms_skill_data.py
python3 ./manage.py shell < ./seed/scripts/curriculum_vitae/skills/import_webserver_skill_data.py
python3 ./manage.py shell < ./seed/scripts/project/import_project_data.py
python3 ./manage.py shell < ./seed/scripts/project/import_project_resource_data.py
python3 ./manage.py shell < ./seed/scripts/timesheet/import_timesheet_data.py
python3 ./manage.py shell < ./seed/scripts/timesheet/import_timesheet_task_data.py
python3 ./manage.py shell < ./seed/scripts/build_team/import_project_request_data.py
python3 ./manage.py shell < ./seed/scripts/build_team/import_configured_role_data.py
python3 ./manage.py shell < ./seed/scripts/build_team/import_configured_role_skill_data.py
python3 ./manage.py shell < ./seed/scripts/build_team/import_team_composition_data.py