from rest_framework import generics

from distributor.api import serializers as dist_ser
from distributor.models.DistributorModel import Distributor

class DistributorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Distributor.objects.all()
    serializer_class = dist_ser.DistributorSerializer


class DistributorUpdateRetrieveDestroyAPIVIew(generics.RetrieveUpdateDestroyAPIView):
    queryset = Distributor.objects.all()
    serializer_class = dist_ser.DistributorSerializer
    lookup_field = 'pk'




