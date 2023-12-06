# In your test file (e.g., tests.py)
from django.test import TestCase
from django.core.wsgi import get_wsgi_application

class WSGITestCase(TestCase):
    def test_wsgi_application(self):
        application = get_wsgi_application()
        self.assertIsNotNone(application)
