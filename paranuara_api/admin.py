from django.contrib import admin

from paranuara_api.models import Company, Foodstuff, Person, Tag


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('index', 'company_name')

@admin.register(Foodstuff)
class FoodstuffAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('label',)
