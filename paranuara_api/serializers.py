from rest_framework import serializers

from paranuara_api.models import Company

class CompanyListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='company-detail',
                                               lookup_field='index')
    class Meta:
        model = Company
        fields = ('index', 'company_name', 'url')

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('index', 'company_name')
