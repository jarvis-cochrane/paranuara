import json
import logging
import sys

from paranuara_api.models import Company, Tag, Foodstuff

logger = logging.getLogger(__name__)

# TODO: Refactor the exception handling and logging as a decorator
#       which could be used like this:
#
# @log_exception('Error creating company')
# def _import_company(data):
#     return Company.objects.create(...)
#
def _log_exception(msg, e):
        e_type, e_value, _ = sys.exc_info()
        logger.error('%s (%s: %s)', msg, e_type, e_value)


def _import_company(data):
    """
    Create and save a new Company instance initialised with the data
    in the supplied dictionary `data`.
    `data` must contain the keys `index` and `company`
    """
    logger.debug('_import_company(): %s', data)

    # TODO: More detailed validation and error reporting
    try:
        return Company.objects.create(
                index=data['index'], 
                company_name=data['company'])
    except Exception as e:
        _log_exception('Error creating company', e)
    return None


def import_companies(fp):
    logger.info('Importing companies')

    return json.load(fp, object_hook=_import_company)


def _import_tag(label):
    """
    Return a Tag instance for the supplied `label` value, creating it
    if it doesn't exist.
    """
    logger.debug('_import_tag(): %s', label)
    try:
        (tag, _) =  Tag.objects.get_or_create(
                        label=label, 
                        defaults={'label': label})
        return tag
    except Exception as e:
        _log_exception('Error importing tag', e)
    return None


def _import_foodstuff(name):
    """
    Return a Foodstuff instance for the supplied `name` value, creating it
    if it doesn't exist. Newly created Foodstuff instances will be assigned
    type='Vegetable'.
    """
    logger.debug('_import_foodstuff(): %s', name)
    try:
        (foodstuff, _) = Foodstuff.objects.get_or_create(
                            name=name, 
                            defaults={'name': name, 
                                      'type': Foodstuff.VEGETABLE})
        return foodstuff
    except Exception as e:
        _log_exception('Error importing foodstuff', e)
    return None
