from django.contrib import admin
from django.urls import path, include

from core.drf_yasg import urlpatterns as swagger_urlpatterns

urlpatterns_api = [
    path('distributor/', include('distributor.urls')),
    path('item/', include('item.urls')),

]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(urlpatterns_api))
] + swagger_urlpatterns


