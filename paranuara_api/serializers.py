from rest_framework import serializers

from paranuara_api.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('index', 'company_name')
