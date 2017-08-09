from django.contrib import admin

from paranuara_api.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('index', 'company_name')
