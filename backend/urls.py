
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.viewsets.stateViewSet import StateViewSet
from api.viewsets.cityViewSet import CityViewSet
from api.viewsets.campusViewSet import *


route = routers.DefaultRouter()
route.register(r'states', StateViewSet)
route.register(r'cities', CityViewSet)
route.register(r'campus', CampusViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include(route.urls))
    path('', include('api.urls'))
]
