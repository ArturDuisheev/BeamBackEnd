from django.urls.conf import path
from item.api import views

urlpatterns = [
    path('create/', views.ItemListCreateAPIView.as_view(), name='list-create'),
    path('detail/<int:pk>/', views.ItemDetailAPIView.as_view(), name='detail'),
]