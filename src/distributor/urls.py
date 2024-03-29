from django.urls.conf import path, include

from distributor.api import views 
from distributor.templates.views import DistributorListCreateView as views_temp_create

urlpatterns_tempates = [
    path('create_template/', views_temp_create.distributor_list_create, name='create_template')
]

urlpatterns = [
    path('create/', views.DistributorListCreateAPIView.as_view(), name='dist-list-create'),
    path('detail/<int:pk>/', views.DistributorUpdateRetrieveDestroyAPIVIew.as_view(), name='dist-detail'),
    path('templates/', include(urlpatterns_tempates))
]