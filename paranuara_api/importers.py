import json
import logging
import sys

from paranuara_api.models import Company

logger = logging.getLogger(__name__)

def _import_company(data):
    """
    Create and save a new Company instance initialised with the data
    in the supplied dictionary `data`.
    `data` must contain the keys `index` and `company`
    """
    logger.debug('_make_company(): %s', data)

    # TODO: More detailed validation and error reporting
    try:
        company = Company()
        company.index = data['index']
        company.company_name = data['company']
        company.save()
        return company
    except Exception as e:
        e_type, e_value, _ = sys.exc_info()
        logger.error('Error creating company (%s: %s)', e_type, e_value)
    return None


def import_companies(fp):
    logger.info('Importing companies')

    return json.load(fp, object_hook=_import_company)
