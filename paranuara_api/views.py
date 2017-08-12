from rest_framework import viewsets

from paranuara_api.models import Company, Person
from paranuara_api.serializers import (
        CompanySerializer, CompanyListSerializer, PersonListSerializer,
        PersonSerializer
)

class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Company.objects.all()
    lookup_field = 'index'

    serializers = {
        'list': CompanyListSerializer,
        'retrieve': CompanySerializer,
    }

    def get_serializer_class(self):
        return self.serializers[self.action]


class PersonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Person.objects.all()
    lookup_field = 'index'

    serializers = {
        'list': PersonListSerializer,
        'retrieve': PersonSerializer,
    }

    def get_serializer_class(self):
        return self.serializers[self.action]

