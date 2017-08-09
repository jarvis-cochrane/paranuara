from django.core.exceptions import ValidationError
from django.test import TestCase

from paranuara_api.importers import _import_company, import_companies

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
