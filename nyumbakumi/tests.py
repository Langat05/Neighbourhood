from django.test import TestCase
from .models import neighbourhood,healthservices
from django.contrib.auth.models import User
# Create your tests here.

class neighbourhoodTestClass(TestCase):
    def setUp(self):
        self.kataret = neighbourhood(neighbourhood='Kataret')

    def test_instance(self):
        self.assertTrue(isinstance(self.Kataret,neighbourhood))

    def tearDown(self):
        neighbourhood.objects.all().delete()

    def test_save_method(self):
        self.Kataret.save_neighbourhood()
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete_method(self):
        self.Kataret.delete_neighbourhood('Kataret')
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood)==0)