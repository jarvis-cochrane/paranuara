from rest_framework import viewsets

from paranuara_api.models import Company
from paranuara_api.serializers import CompanySerializer, CompanyListSerializer

class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Company.objects.all()
    lookup_field = 'index'

    serializers = {
        'list': CompanyListSerializer,
        'retrieve': CompanySerializer,
    }

    def get_serializer_class(self):
        return self.serializers[self.action]
