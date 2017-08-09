from django.db import models


class Company(models.Model):
    """
    A Paranuaran company.
    """

    # The index of the company record in the JSON source data
    index = models.PositiveIntegerField(unique=True)

    # Referred to as 'company' in the JSON source data
    company_name = models.CharField(unique=True, max_length=100)

    class Meta:
        ordering = ['company_name']
        verbose_name_plural = 'Companies'


class Foodstuff(models.Model):
    """
    A kind of food - initially either a fruit or a vegetable
    """
    FRUIT = 'f'
    VEGETABLE = 'v'

    TYPE_CHOICES = (
        (FRUIT, 'Fruit'),
        (VEGETABLE, 'Vegetable'),
    )

    name = models.CharField(unique=True, max_length=100)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Foodstuffs'


class Tag(models.Model):
    """
    A tag which can be linked to a Person
    """
    label = models.CharField(unique=True, max_length=100)

    class Meta:
        ordering = ['label']
        verbose_name_plural = 'Tags'


class Person(models.Model):
    """
    A Paranuaran Person
    """
    EYE_COLOR_BLUE = 'bl'
    EYE_COLOR_BROWN = 'br'
    EYE_COLOR_CHOICES = (
        (EYE_COLOR_BLUE, 'Blue'),
        (EYE_COLOR_BROWN, 'Brown'),
    )

    GENDER_MALE = 'm'
    GENDER_FEMALE = 'f'
    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
    )

    # The _id field from the JSON source file
    json_id = models.CharField(unique=True, max_length=24)

    # The index of of the Person record in the JSON file
    index = models.PositiveIntegerField(unique=True)

    guid = models.CharField(unique=True, max_length=36)

    has_died = models.BooleanField()

    balance = models.DecimalField(max_digits=8,decimal_places=2)

    picture = models.URLField()

    age = models.PositiveIntegerField()

    eyecolor = models.CharField(max_length=2, choices = EYE_COLOR_CHOICES)

    name = models.CharField(max_length=100)

    gender = models.CharField(max_length=1, choices = GENDER_CHOICES)

    company = models.ForeignKey(Company)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=30)

    address = models.CharField(max_length=200)

    about = models.TextField()

    registered = models.DateTimeField()

    tags = models.ManyToManyField(Tag)

    friends = models.ManyToManyField('Person')

    greeting = models.CharField(max_length=100)

    favourite_food = models.ManyToManyField(Foodstuff)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'People'
