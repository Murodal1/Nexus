from django.test import TestCase
from django.urls import resolve, reverse

class CategoryURLTest(TestCase):
    def test_category_list_url_resolves(self):
        url = reverse('category_list')
        self.assertEqual(resolve(url).func, category_list_view)