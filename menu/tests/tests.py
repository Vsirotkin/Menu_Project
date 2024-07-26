from django.test import TestCase, Client
from django.urls import reverse


class MenuViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "menu/home.html")

    def test_about_view(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "menu/about.html")

    def test_team_view(self):
        response = self.client.get(reverse("team"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "menu/team.html")

    def test_history_view(self):
        response = self.client.get(reverse("history"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "menu/history.html")

    def test_contact_view(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "menu/contact.html")
