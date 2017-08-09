from datetime import datetime
import json
import logging
import re
import sys

from django.core.exceptions import ObjectDoesNotExist

from paranuara_api.models import Company, Tag, Foodstuff, Person

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

# Compiled Regex that will match only digits and the decimal point
_non_decimal = re.compile(r'[^\d.]+')

def _parse_currency(currency):
    """
    Convert strings containing currency symbols and commas to 
    plain decimal strings
    """
    return _non_decimal.sub('', currency)

def _parse_timestamp(ts):
    """
    Convert the provided timestamp format to a Python datetime+TZ
    """
    # remove the unhelpful colon in the TZ specification
    ts = ts[0:-3]+ts[-2:]
    return datetime.strptime(ts, '%Y-%m-%dT%H:%M:%S %z')

def _parse_choices(choices, value):
    for (k, v) in choices:
        if (v.lower()==value.lower()):
            return k
    raise ValidationError('Invalid choice {}'.format(value))


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

def _import_person(data):
    """
    Create and save a new Person instance initialised with the data
    in the supplied dictionary `data`.
    """
    logger.debug('_import_person(): %s', data['name'])

    try:

        # Look up the associated company

        try:
            company = Company.objects.get_for_index(data['company_id'])
        except ObjectDoesNotExist:
            company = None

        person =  Person.objects.create(
                    json_id=data['_id'],
                    index=data['index'],
                    guid=data['guid'],
                    has_died=data['has_died'],
                    balance=_parse_currency(data['balance']),
                    picture=data['picture'],
                    age=data['age'],
                    eyecolor=_parse_choices(Person.EYE_COLOR_CHOICES,
                                            data['eyeColor']),
                    name=data['name'],
                    gender=_parse_choices(Person.GENDER_CHOICES, 
                                          data['gender']),
                    email=data['email'],
                    phone=data['phone'],
                    address=data['address'],
                    about=data['about'],
                    registered=_parse_timestamp(data['registered']),
                    greeting = data['greeting'],
                    company=company)
    except Exception as e:
        _log_exception('Error importing person', e)
    return None

def _relate_person(data):
    """
    Set up the relationships that require either the Person instance to have
    a valid id, or for all People to have been imported
    """
    logger.debug('_relate_person(): %s', data['name'])

    try:
        person = Person.objects.get(json_id=data['_id'])
        person.tags = [_import_tag(x) for x in data['tags']]
        person.favourite_food = (
            [_import_foodstuff(x) for x in data['favouriteFood']])
        person.save()
        return person
    except Exception as e:
        _log_exception('Error relating person', e)
    return None


def import_people(fp):
    logger.info('Importing people')

    parsed_json = json.load(fp)

    [_import_person(x) for x in parsed_json]
    return [_relate_person(x) for x in parsed_json]
