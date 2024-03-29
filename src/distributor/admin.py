from django.contrib import admin

from distributor.models.DistributorModel import Distributor


class DistributorAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email')

admin.site.register(Distributor, DistributorAdmin)
