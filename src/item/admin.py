from django.contrib import admin

from item.models.ItemModel import Item, Category

admin.site.register(Item)
admin.site.register(Category)
