import logging

from paranuara_api.importers import import_people
from paranuara_api.management.base import BaseImportCommand

logger = logging.getLogger(__name__)


class Command(BaseImportCommand):
    help = 'Import person data from the specified file'

    def _import(self, fp):
        import_people(fp)
