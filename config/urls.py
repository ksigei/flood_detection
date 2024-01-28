from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Ndanu API",
        default_version='v1',
        description="Ndanu API description",
        terms_of_service="#",
        contact=openapi.Contact(email="#"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('endpoints.urls')),
    # path('api-auth/', include('rest_framework.urls')),
    path('predictions/', include('predictions.urls')),
    path('', include('sensors.urls')),
    path('', include('alerts.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
