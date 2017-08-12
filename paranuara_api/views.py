from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from paranuara_api.models import Company, Person
from paranuara_api.serializers import (
        CompanySerializer, CompanyListSerializer, PersonListSerializer,
        PersonSerializer, FriendshipSerializer
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

class Friendship(object):

    def __init__(self, person, friend, friends):
        self.person = person
        self.friend = friend
        self.friends = friends


class FriendsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Person.objects.all()
    lookup_field = 'index'

    serializers = {
        'list': CompanyListSerializer,
        'retrieve': CompanySerializer,
    }

    def list(self, request, person_index=None):
        person = get_object_or_404(Person, index=person_index)
        serializer = PersonListSerializer(person.friends.is_alive(), 
                                          many=True,
                                          context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, index=None, person_index=None): 
        person = get_object_or_404(Person, index=person_index)
        friend = get_object_or_404(Person, index=index)
        friends = (Person.objects.has_friend(person).has_friend(friend).
                   has_brown_eyes().is_alive())
        friendship = Friendship(person, friend, friends)
        serializer = FriendshipSerializer(friendship)
        return Response(serializer.data)

