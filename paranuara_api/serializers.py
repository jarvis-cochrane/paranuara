from rest_framework import serializers

from paranuara_api.models import Company, Person, Foodstuff


class BasePersonSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='person-detail',
                                               lookup_field='index')


class PersonListSerializer(BasePersonSerializer):
    class Meta:
        model = Person
        fields = ('name', 'url')


class PersonSerializer(BasePersonSerializer):
    username = serializers.CharField(source='name')
    fruits = serializers.StringRelatedField(source='favourite_fruit', 
                                            many=True)
    vegetables = serializers.StringRelatedField(source='favourite_vegetables',
                                                many=True)

    class Meta:
        model = Person
        fields = ('username', 'age', 'fruits', 'vegetables')


class EmployeeSerializer(BasePersonSerializer):
    class Meta:
        model = Person
        fields = ('name', 'has_died', 'url')


class BaseCompanySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='company-detail',
                                               lookup_field='index')


class CompanyListSerializer(BaseCompanySerializer):
    class Meta:
        model = Company
        fields = ('index', 'company_name', 'url')


class CompanySerializer(BaseCompanySerializer):
    current_employees = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ('index', 'company_name', 'url', 'current_employees')
