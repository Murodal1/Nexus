from django.test import TestCase
from django.urls import reverse, resolve

class ViewTest(TestCase):
    def test_login_view_status_code(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code,200)

    def test_login_view_template_used(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'login.html')

    def test_register_view_status_code(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code,200)

    def test_register_view_template_used(self):
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed(response, 'register.html')

    def test_logout_view_status_code(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code,302)

    def test_logout_view_template_used(self):
        response = self.client.get(reverse('main'))
        self.assertTemplateUsed(response, 'index.html')