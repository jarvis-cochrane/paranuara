from django.db import models


class Company(models.Model):
    """
    A Paranuaran company.
    """

    # The index of the company record in the JSON source data
    index = models.PositiveIntegerField()

    # Referred to as 'company' in the JSON source data
    company_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['company_name']
        verbose_name_plural = 'Companies'
