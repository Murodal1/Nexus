from django.test import TestCase
from django.urls import reverse, resolve

class ViewTest(TestCase):
    def test_blog_view_status_code(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code,200)

    def test_blog_view_template_used(self):
        response = self.client.get(reverse('blog'))
        self.assertTemplateUsed(response, 'blog.html')