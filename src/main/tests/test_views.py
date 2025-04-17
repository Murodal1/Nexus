from django.test import TestCase
from django.urls import reverse, resolve
from ..views import main, about, contact, services

class ViewTest(TestCase):
    def test_main_view_status_code(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code,200)

    def test_main_view_template_used(self):
        response = self.client.get(reverse('main'))
        self.assertTemplateUsed(response, 'index.html')


