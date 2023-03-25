from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from decouple import config


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        if User.objects.count() == 0:
            username = config("DJANGO_ADMIN_USER")
            password = config("DJANGO_ADMIN_PASSWORD")
            email = config("DJANGO_ADMIN_EMAIL")
            User.objects.create(
                is_superuser=True, username=username, password=password, email=email
            )
            print(f"User {username} created ...")
        else:
            print("fails to create superUser, previus user exist...")
