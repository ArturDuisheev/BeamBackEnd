from rest_framework import generics

from item.models import ItemModel as item_mod
from item.api import serializers as item_ser

class ItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = item_mod.Item.objects.all()
    serializer_class = item_ser.ItemSerializer

class ItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = item_mod.Item.objects.all()
    serializer_class = item_ser.ItemSerializer
    lookup_field = 'pk'