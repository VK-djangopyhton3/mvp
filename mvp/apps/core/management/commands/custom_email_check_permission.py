from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group, Permission

User = get_user_model()

class Command(BaseCommand):
    help = 'This is for create check email permission'

    def add_arguments(self, parser):
        # parser.add_argument('', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        # Code to add permission to group
        ct = ContentType.objects.get_for_model(User)

        permission, created = Permission.objects.get_or_create(codename='can_check_email', name='Can check email!', content_type=ct)
        new_group, created = Group.objects.get_or_create(name='EmailValidator')
        new_group.permissions.add(permission)
        self.stdout.write(self.style.SUCCESS('Permission successfully created or retrieved'))
