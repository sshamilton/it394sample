from django.test import TestCase
from users.models import Cadet

class CadetTestCase(TestCase):
    def setUp(self):
        Cadet.objects.create(first="John", last="Doe", xnumber="x91111")
        Cadet.objects.create(first="Jane", last="Doe", xnumber="x92222")

    def test_cadets_(self):
        """All cadets should have an xnumber, first, and last name"""
        johndoe = Cadet.objects.get(xnumber="x91111")
        janedoe = Cadet.objects.get(xnumber="x92222")
        self.assertEqual(johndoe.name(), 'Doe, John')
        self.assertEqual(janedoe.name(), 'Doe, Jane')

