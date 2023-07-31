import os
import django

from core.models.account.account import AccountModel


def main():
    # Admin user
    AccountModel.objects.create_superuser(username='admin@admin.com', email='admin@admin.com', password='pass@123')


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humancloud.settings')
django.setup()

if __name__ == "__main__":
    main()
else:
    main()
