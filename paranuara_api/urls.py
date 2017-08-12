from django.conf.urls import url, include
from rest_framework_nested import routers

from paranuara_api import views

router = routers.DefaultRouter()
router.register(r'companies', views.CompanyViewSet)
router.register(r'people', views.PersonViewSet)

friends_router = routers.NestedSimpleRouter(router, r'people', lookup='person')
friends_router.register('friends', views.FriendsViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(friends_router.urls)),
]
