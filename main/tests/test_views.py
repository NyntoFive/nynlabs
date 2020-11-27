from django.test import TestCase
from django.contrib.urls import reverse

from decimal import Decimal
from main import models

class TestPage(TestCase):
    def test_home_page_works(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/home.html')
        self.assertContains(response, "Nynlabs.com")

    def test_about_page_works(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/about.html')
        self.assertContains(response, "About")

    def test_contact_view_works(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/contact_form.html')
        self.assertContains(response, "Nynlabs")
        self.assertIsInstance(
            response.context["form"], forms.ContactForm
        )
    
    def test_products_page_returns_active(self):
        models.Product.objects.create(
            name="None ever talked about a cathedral and a bazaar.",
            slug="cathedral-bazaar",
            price=Decimal("10.00")
        )
        models.Product.objects.create(
            name="This is a name for a product",
            slug="product-name-slug",
            price=Decimal("9.50")
        )
        models.Product.objects.create(
            name="A Tale of Three Children",
            slug="tale-three-children",
            price=Decimal("19.50"),
            active=False,
        )
        response = self.client.get(
            reverse("products", kwargs={"tag": "all"})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nynlabs")
        
        product_list = models.Product.objects.active().order_by("name")
        self.assertEqual(
            list(response.context["object_list"]),
            list(product_list)
        )
    def test_products_page_filters_by_tags_and_active(self):
        cb = models.Product.objects.create(
            name="The cathedral and the bazaar",
            slug="cathedral-bazaar",
            price=Decimal("10.00"),
        )
        
        cb.tags.create(name="Open source", slug="opensource")
        models.Product.objects.create(
            name="Microsoft Windows guide",
            slug="microsoft-windows-guide",
            price=Decimal("12.00"),
        )
        response = self.client.get(
            reverse("products", kwargs={"tag": "opensource"})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nynlabs")
        product_list = (
            models.Product.objects.active()
            .filter(tags__slug="opensource")
            .order_by("name")
        )
        
        self.assertEqual(
            list(response.context["object_list"]),
            list(product_list),
 )