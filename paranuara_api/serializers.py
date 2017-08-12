from rest_framework import serializers

from paranuara_api.models import Company, Person

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'has_died')

class CompanyListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='company-detail',
                                               lookup_field='index')
    class Meta:
        model = Company
        fields = ('index', 'company_name', 'url')

class CompanySerializer(serializers.ModelSerializer):

    current_employees = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ('index', 'company_name', 'current_employees')
