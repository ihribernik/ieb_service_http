"""
"""
from decouple import config, Csv
from ieb_service_http.settings.base import *  # NOQA

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())
DEBUG = True
