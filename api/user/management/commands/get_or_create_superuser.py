from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates a superuser if it does not exist'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username of the superuser')
        parser.add_argument('email', type=str, help='Email of the superuser')
        parser.add_argument('password', type=str, help='Password of the superuser')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        email = kwargs['email']
        password = kwargs['password']

        try:
            if User.objects.filter(email=email).exists():
                self.stdout.write(self.style.WARNING(f'Superuser with email {email} already exists.'))
            elif User.objects.filter(username=username).exists():
                self.stdout.write(self.style.WARNING(f'Superuser with username {username} already exists.'))
            else:
                User.objects.create_superuser(email, password, username=username) #type: ignore
                self.stdout.write(self.style.SUCCESS(f'Superuser {username} created successfully.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating superuser: {str(e)}'))
