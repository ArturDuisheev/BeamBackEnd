from rest_framework import serializers

from distributor.models.DistributorModel import Distributor

class DistributorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Distributor
        fields = (
            'id',
            'fullname', 
            'email',
            'item',
            'created_at'
            )
        
    