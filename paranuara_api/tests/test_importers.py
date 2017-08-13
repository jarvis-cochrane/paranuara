from django.core.exceptions import ValidationError
from django.test import TestCase

from paranuara_api.importers import (
        _import_company, _import_foodstuff, _import_foodstuff_from_json,
        _import_tag, _parse_choices, _parse_currency, _parse_timestamp,
        import_companies,
)
from paranuara_api.models import Foodstuff, Tag


# TODO: More extensive test cases

class ParseCurrencyTestCase(TestCase):

    def test_parse_currency(self):
        self.assertEqual(_parse_currency('$1,234.56'), '1234.56')


class ParseTimestampTestCase(TestCase):

    def test_parse_timestamp(self):
        self.assertEqual(
                _parse_timestamp('2017-08-10T18:50:01 +10:00').isoformat(),
                '2017-08-10T18:50:01+10:00')


class ParseChoicesTestCase(TestCase):

    CHOICES = (
        ('a', 'Alpha'),
        ('b', 'Beta'),
    )

    def test_parse_choices_match_exact(self):
        self.assertEqual(_parse_choices(self.CHOICES, 'Alpha'), 'a')

    def test_parse_choices_match_mixed_case(self):
        self.assertEqual(_parse_choices(self.CHOICES, 'aLpHa'), 'a')

    def test_parse_choices_no_match(self):
        with self.assertRaises(ValidationError):
            _parse_choices(self.CHOICES, 'pony')


class ImportCompanyTestCase(TestCase):

    def test_import_company_normal(self):
        data = {'index': 0, 'company': 'Nostromo'}

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
        Tag.objects.create(label='tame')
        self.assertEqual(len(Tag.objects.all()), 1)

        tag = _import_tag('tame')

        self.assertEqual(len(Tag.objects.all()), 1)
        self.assertEquals(tag.label, 'tame')


class ImportFoodstuffTestCase(TestCase):

    def test_import_foodstuff_new_with_default(self):
        self.assertFalse(Foodstuff.objects.exists())

        foodstuff = _import_foodstuff('leek')

        self.assertEqual(len(Foodstuff.objects.all()), 1)
        self.assertIsNotNone(foodstuff.id)
        self.assertEquals(foodstuff.name, 'leek')
        self.assertEquals(foodstuff.type, Foodstuff.VEGETABLE)

    def test_import_foodstuff_new_fruit(self):
        self.assertFalse(Foodstuff.objects.exists())

        foodstuff = _import_foodstuff('olive', type=Foodstuff.FRUIT)

        self.assertEqual(len(Foodstuff.objects.all()), 1)
        self.assertIsNotNone(foodstuff.id)
        self.assertEquals(foodstuff.name, 'olive')
        self.assertEquals(foodstuff.type, Foodstuff.FRUIT)

    def test_import_foodstuff_exists(self):
        Foodstuff.objects.create(
                                name='apple',
                                type=Foodstuff.FRUIT)
        self.assertEqual(len(Foodstuff.objects.all()), 1)

        foodstuff = _import_foodstuff('apple')

        self.assertEqual(len(Foodstuff.objects.all()), 1)
        self.assertEquals(foodstuff.name, 'apple')
        self.assertEquals(foodstuff.type, Foodstuff.FRUIT)


class ImportFoodStuffFromJSONTestCase(TestCase):

    def test_import_food_stuff_from_json_new(self):
        self.assertFalse(Foodstuff.objects.exists())

        json = {'name': 'pear', 'type': Foodstuff.FRUIT}

        foodstuff = _import_foodstuff_from_json(json)

        self.assertEqual(len(Foodstuff.objects.all()), 1)
        self.assertEquals(foodstuff.name, 'pear')
        self.assertEquals(foodstuff.type, Foodstuff.FRUIT)
