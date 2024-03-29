from rest_framework import serializers

from item.models import ItemModel as item_mod

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = item_mod.Category
        fields = ('id', 'name')

class ItemSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField('get_category')

    class Meta:
        model = item_mod.Item
        fields = ('id', 'product', 'quantity', 'category') 

    def get_category(self, obj):
        return obj.category.name