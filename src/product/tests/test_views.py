from django.test import TestCase
from django.urls import reverse, resolve

class ViewTest(TestCase):
    def test_product_list_view_status_code(self):
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code,200)

    def test_product_list_view_template_used(self):
        response = self.client.get(reverse('product-list'))
        self.assertTemplateUsed(response, 'products.html')

    # def test_product_detail_view_status_code(self):
    #     response = self.client.get(reverse('product-detail'))
    #     self.assertEqual(response.status_code,200)
    #
    # def test_product_detail_view_template_used(self):
    #     response = self.client.get(reverse('product-detail'))
    #     self.assertTemplateUsed(response, 'detail.html')

    def test_product_add_view_status_code(self):
        response = self.client.get(reverse('product-add'))
        self.assertEqual(response.status_code,200)

    def test_product_add_view_template_used(self):
        response = self.client.get(reverse('product-add'))
        self.assertTemplateUsed(response, 'product_add.html')