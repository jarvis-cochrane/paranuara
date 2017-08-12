from rest_framework import viewsets

from paranuara_api.models import Company, Person
from paranuara_api.serializers import (
        CompanySerializer, CompanyListSerializer, PersonListSerializer,
        PersonSerializer
)

class MultiSerializerMixin(object):

    def get_serializer_class(self):
        return self.serializers[self.action]


class CompanyViewSet(MultiSerializerMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Company.objects.all()
    lookup_field = 'index'

    serializers = {
        'list': CompanyListSerializer,
        'retrieve': CompanySerializer,
    }


class PersonViewSet(MultiSerializerMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Person.objects.all()
    lookup_field = 'index'

    serializers = {
        'list': PersonListSerializer,
        'retrieve': PersonSerializer,
    }

