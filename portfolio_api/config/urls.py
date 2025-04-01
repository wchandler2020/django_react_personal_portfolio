from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title = "William Chandler Portfolio API",
        default_version = "v1",
        description = "this is the documentation for the backend api for the portfolio API",
        terms_of_service = "http://mywebsite.com/policies/",
        contact = openapi.Contact(email="vastyle2010@gmail.com"),
        license = openapi.License(name="WDC License")
    ),
    public = True,
    permission_classes = (permissions.AllowAny, )
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/', include('portfolio.urls')),

    ####API documentation#####
    path("", schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
