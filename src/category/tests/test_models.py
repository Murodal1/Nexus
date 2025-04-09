from django.test import TestCase
from category.models import Category, Region, Brand

class CategoryModelTest(TestCase):
    def create_category(self):
        category = Category.objects.create(
            name="Elektronika",
            is_main=True,
            slug="elektronika"
        )
        self.assertEqual(category.name, "Elektronika")
        self.assertTrue(category.is_main)
        self.assertEqual(category.slug, "elektronika")
        self.assertIsNone(category.parent)

    def test_create_subcategory(self):
        parent = Category.objects.create(name="Elektronika", slug="elektronika")
        sub = Category.objects.create(
            name="Telefonlar",
            slug="telefonlar",
            parent=parent
        )
        self.assertEqual(sub.parent, parent)

class RegionModelTest(TestCase):
    def test_create_region(self):
        region = Region.objects.create(name="Tashkent", sorting=1)
        self.assertEqual(region.name,"Tashkent")
        self.assertEqual(region.sorting,1)

class BranModelTest(TestCase):
    def test_create_brand(self):
        brand = Brand.objects.create(name="Samsung")
        self.assertEqual(brand.name,"Samsung")