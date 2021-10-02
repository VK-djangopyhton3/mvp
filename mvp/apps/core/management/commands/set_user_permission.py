from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group, Permission

User = get_user_model()


class Command(BaseCommand):
    help = 'This is for create translator permission'

    def add_arguments(self, parser):
        # parser.add_argument('', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        try:
            # Code to add permission to group
            users = User.objects.filter(is_active=True, is_staff=False)
            for user in users:
                permission = None
                if user.groups.filter(name="Translator").exists():
                    permission = Permission.objects.get(codename='can_translate')

                if user.groups.filter(name="EmailValidator").exists():
                    permission = Permission.objects.get(codename='can_check_email')

            user.user_permissions.add(permission)
            self.stdout.write(self.style.SUCCESS('Permission successfully added'))
        except Exception as e:
            self.stdout.write(self.style.ERROR('Failed to add permission with user'))
