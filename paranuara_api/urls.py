from django.conf.urls import url, include
from rest_framework import routers

from paranuara_api import views

router = routers.DefaultRouter()
router.register(r'companies', views.CompanyViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
