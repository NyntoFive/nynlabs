from django.test import TestCase
from django.contrib.urls import reverse
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
