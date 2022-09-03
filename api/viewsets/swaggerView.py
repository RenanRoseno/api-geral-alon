from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Posts API",
        default_version='1.0.0',
        description="API de Gerenciamento de Protocolos",
    ),
    public=True,
)

swagger_view = include([
    path('/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
])
