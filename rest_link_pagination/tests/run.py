from django.conf import settings
import django
import os
import sys

sys.path.insert(1, os.path.join(os.path.dirname(__file__), "..", ".."))

settings.configure(
    INSTALLED_APPS=["rest_link_pagination"],
    ROOT_URLCONF="rest_link_pagination.tests.urls",
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
        }
    }
)

try:
    django.setup()
except AttributeError:
    # Django 1.7+
    pass

from django.test.utils import get_runner

TestRunner = get_runner(settings)
runner = TestRunner()

failures = runner.run_tests(["rest_link_pagination"])
