import logging

from django.core.management.base import BaseCommand

from paranuara_api.importers import import_people


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'import person data from the specified file'

    def add_arguments(self, parser):
        parser.add_argument('person_file')

    def handle(self, *args, **options):
        logger.debug('person_file: ', options['person_file'])
        try:
            with open(options['person_file'], 'r') as fp:
                logger.debug('starting import')
                people = import_people(fp)
                logger.info('imported %d people', len(people))
        except Exception as e:
            logger.exception(e)
