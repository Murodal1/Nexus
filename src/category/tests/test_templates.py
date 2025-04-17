# from django.test import TestCase
# from category.models import Category
#
# class CategoryTemplateRenderingTest(TestCase):
#     def setUp(self):
#         self.category = Category.objects.create(
#             name="Elektronika", slug="elektronika", is_main=True
#         )
#
#     def test_category_li_template_content(self):
#         response = self.client.get(reverse('category_list'))
#         self.assertContains(response, "Elektronika")