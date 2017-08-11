import logging

from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)

class BaseImportCommand(BaseCommand):

    def _import(self, fp):
        """
        Abstract method to import data from the supplied open file object
        """
        pass

    def add_arguments(self, parser):
        parser.add_argument('json_file')

    def handle(self, *args, **options):
        logger.debug('json_file: ', options['json_file'])
        try:
            with open(options['json_file'], 'r') as fp:
                logger.debug('starting import')
                self._import(fp)
                logger.info('import completed')
        except Exception as e:
            logger.exception(e)
