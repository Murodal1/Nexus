# from django.test import TestCase
# from category.forms import CategoryForm
#
# class CategoryFormTest(TestCase):
#     def test_valid_form(self):
#         form_data = {
#             'name': 'Telefonlar',
#             'slug': 'telefonlar',
#             'is_main': False
#         }
#         form = CategoryForm(data=form_data)
#         self.assertTrue(form.is_valid())
#
#     def test_invalid_form(self):
#         form_data = {
#             'slug': '',
#         }
#         form = CategoryForm(data=form_data)
#         self.assertFalse(form.is_valid())
#         self.assertIn('slug', form.errors)