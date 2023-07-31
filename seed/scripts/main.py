from seed.scripts.import_data import main as import_data
from seed.scripts.client.import_client_data import main as import_client_data
from seed.scripts.client.import_client_accounts_data import main as import_client_accounts_data
from seed.scripts.partner.import_partner_data import main as import_partner_data
from seed.scripts.partner.import_partner_accounts_data import main as import_partner_accounts_data
from seed.scripts.resource.import_resource_data import main as import_resource_data
from seed.scripts.resource.import_resource_contract_details_data import main as import_resource_contract_details_data
from seed.scripts.support.import_support_accounts_data import main as import_support_accounts_data
from seed.scripts.curriculum_vitae.import_curriculum_vitae_data import main as import_curriculum_vitae_data
from seed.scripts.curriculum_vitae.import_domain_expertise_data import main as import_domain_expertise_data
from seed.scripts.curriculum_vitae.import_certification_data import main as import_certification_data
from seed.scripts.curriculum_vitae.import_education_history_data import main as import_education_history_data
from seed.scripts.curriculum_vitae.import_employment_history_data import main as import_employment_history_data
from seed.scripts.curriculum_vitae.import_employment_project_data import main as import_employment_project_data
from seed.scripts.curriculum_vitae.skills.import_cloud_skill_data import main as import_cloud_skill_data
from seed.scripts.curriculum_vitae.skills.import_framework_skill_data import main as import_framework_skill_data
from seed.scripts.curriculum_vitae.skills.import_language_skill_data import main as import_language_skill_data
from seed.scripts.curriculum_vitae.skills.import_no_sql_skill_data import main as import_no_sql_skill_data
from seed.scripts.curriculum_vitae.skills.import_rdbms_skill_data import main as import_rdbms_skill_data
from seed.scripts.curriculum_vitae.skills.import_webserver_skill_data import main as import_webserver_skill_data
from seed.scripts.project.import_project_data import main as import_project_data
from seed.scripts.project.import_project_resource_data import main as import_project_resource_data
from seed.scripts.timesheet.import_timesheet_data import main as import_timesheet_data
from seed.scripts.timesheet.import_timesheet_task_data import main as import_timesheet_task_data
from seed.scripts.build_team.import_project_request_data import main as import_project_request_data
from seed.scripts.build_team.import_configured_role_data import main as import_configured_role_data
from seed.scripts.build_team.import_configured_role_skill_data import main as import_configured_role_skill_data
from seed.scripts.build_team.import_team_composition_data import main as import_team_composition_data


def run():
    import_data()
    import_client_data()
    import_client_accounts_data()
    import_client_accounts_data()
    import_partner_data()
    import_partner_accounts_data()
    import_resource_data()
    import_resource_contract_details_data()
    import_support_accounts_data()
    import_curriculum_vitae_data()
    import_domain_expertise_data()
    import_certification_data()
    import_education_history_data()
    import_employment_history_data()
    import_employment_project_data()
    import_cloud_skill_data()
    import_framework_skill_data()
    import_language_skill_data()
    import_no_sql_skill_data()
    import_rdbms_skill_data()
    import_webserver_skill_data()
    import_project_data()
    import_project_resource_data()
    import_timesheet_data()
    import_timesheet_task_data()
    import_project_request_data()
    import_configured_role_data()
    import_configured_role_skill_data()
    import_team_composition_data()


if __name__ == '__main__':
    run()
