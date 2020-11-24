from decimal import Decimal
from django.test import TestCase
from main import models

class TestModel(TestCase):
    def test_active_manager_works(self):
        models.Product.objects.create(
            name="The cathedral and the bazaar",
            price=Decimal("10.00"))
        models.Product.objects.create(
            name="Not a model",
            price=Decimal("2.00"))
        models.Product.objects.create(
            name="Coding for stubborn idiots: an Autobiography.",
            price=Decimal("5.00"),
            active=False
            )
        self.assertEqual(len(models.Product.objects.active()), 2)
        