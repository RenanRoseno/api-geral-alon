from django.urls import path, include
from api.viewsets.snippetViewSet import *
from api.viewsets.stateViewSet import *
from api.viewsets.cityViewSet import *
from api.viewsets.campusViewSet import *
from api.viewsets.swaggerView import swagger_view
from rest_framework import routers

route = routers.DefaultRouter()
route.register(r'states', StateViewSet)
route.register(r'cities', CityViewSet, )
route.register(r'campus', CampusViewSet, basename='campus')

urlpatterns = [
    path('', include(route.urls)),
    path('campus-teste', PurchaseList.as_view()),
    path('api-alon/', swagger_view),
    # path('campus-teste/<int:pk>', SnippetDetail.as_view()),
]
