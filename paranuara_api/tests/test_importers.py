from django.core.exceptions import ValidationError
from django.test import TestCase

from paranuara_api.importers import (
        _import_company, import_companies, _import_tag,
        _import_foodstuff
)
from paranuara_api.models import Foodstuff, Tag


# TODO: More extensive test cases

class ImportCompanyTestCase(TestCase):

    def test_import_company_normal(self):
        data = { 'index': 0, 'company': 'Nostromo'}

        company = _import_company(data)

        self.assertIsNotNone(company.id)    # Has been saved
        self.assertEqual(company.index, 0)
        self.assertEqual(company.company_name, 'Nostromo')

    def test_import_company_bad_key(self):
        data = {'company_name': 'Nostromo'}

        company = _import_company(data)

        self.assertIsNone(company)


class ImportCompaniesTestCase(TestCase):

    def test_import_companies(self):
        company_file = 'resources/companies.json'

        with open(company_file, 'r') as fp:
            companies = import_companies(fp)

        self.assertEquals(len(companies), 100)


class ImportTagTestCase(TestCase):

    def test_import_tag_new(self):
        self.assertFalse(Tag.objects.exists())

        tag = _import_tag('lame')

        self.assertEqual(len(Tag.objects.all()), 1)
        self.assertIsNotNone(tag.id)
        self.assertEquals(tag.label, 'lame')

    def test_import_tag_exists(self):
        expected_tag = Tag.objects.create(label='tame')
        self.assertEqual(len(Tag.objects.all()), 1)

        tag = _import_tag('tame')

        self.assertEqual(len(Tag.objects.all()), 1)
        self.assertEquals(tag.label, 'tame')


class ImportFoodstuffTestCase(TestCase):

    def test_import_foodstuff_new(self):
        self.assertFalse(Foodstuff.objects.exists())

        foodstuff = _import_foodstuff('leek')

        self.assertEqual(len(Foodstuff.objects.all()), 1)
        self.assertIsNotNone(foodstuff.id)
        self.assertEquals(foodstuff.name, 'leek')
        self.assertEquals(foodstuff.type, Foodstuff.VEGETABLE)

    def test_import_foodstuff_exists(self):
        expected_foodstuff = Foodstuff.objects.create(
                                name='apple', 
                                type=Foodstuff.FRUIT)
        self.assertEqual(len(Foodstuff.objects.all()), 1)

        foodstuff = _import_foodstuff('apple')

        self.assertEqual(len(Foodstuff.objects.all()), 1)
        self.assertEquals(foodstuff.name, 'apple')
        self.assertEquals(foodstuff.type, Foodstuff.FRUIT)
