import logging

from paranuara_api.importers import import_companies
from paranuara_api.management.base import BaseImportCommand

logger = logging.getLogger(__name__)


class Command(BaseImportCommand):
    help = 'Import company data from the specified file'

    def _import(self, fp):
        import_companies(fp)
