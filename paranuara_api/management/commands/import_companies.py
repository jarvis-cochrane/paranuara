import logging

from django.core.management.base import BaseCommand

from paranuara_api.importers import import_companies


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'import company data from resources/companies.json'

    def add_arguments(self, parser):
        parser.add_argument('company_file')

    def handle(self, *args, **options):
        logger.debug('company_file: ', options['company_file'])
        try:
            with open(options['company_file'], 'r') as fp:
                logger.debug('starting import')
                companies = import_companies(fp)
                logger.info('imported %d companies', len(companies))
        except Exception as e:
            logger.exception(e)
