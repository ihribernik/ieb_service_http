from django.test import SimpleTestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory, force_authenticate
from decouple import config


class TestProductsView(SimpleTestCase):
    def setUp(self) -> None:
        # self.home_url = reverse("home")
        self.username = config("DJANGO_ADMIN_USER")
        self.password = config("DJANGO_ADMIN_PASSWORD")
        self.email = config("DJANGO_ADMIN_EMAIL")
        self.factory = APIRequestFactory()

    def setup_databases(self, **kwargs):
        """Override the database creation defined in parent class"""
        if User.objects.count == 0:
            User.objects.get_or_create(
                username=self.username, password=self.password, email=self.email
            )

    def teardown_databases(self, old_config, **kwargs):
        """Override the database teardown defined in parent class"""
        test_user = User.objects.get(
            username=self.username, password=self.password, email=self.email
        )
        test_user.delete()

    def test_auth(self):
        ...

    def test_products(self):
        ...
