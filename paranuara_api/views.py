from rest_framework import viewsets

from paranuara_api.models import Company
from paranuara_api.serializers import CompanySerializer


class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

