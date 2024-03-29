from django.db import models
from django.utils.translation import gettext_lazy as _ 

from common.models import BaseModel
from item.models.ItemModel import Item

class Distributor(BaseModel):
    fullname = models.CharField(
        _('Полное имя'),
        max_length=120,
    )
    email = models.EmailField(
        _('Почта')
    )
    item = models.ManyToManyField(
        Item, 
        related_name='dist_item',
        verbose_name=_('Продукты'),
        blank=True, null=True
        )


    def __str__(self) -> str:
        return 'Имя: {0}, Почта: {1}'.format(self.fullname, self.email)


    @property
    def group_name(self):
        return "user_%s" % self.id
    
    class Meta:
        verbose_name = _('Дистрибьютер')
        verbose_name_plural = _('Дистрибьютеры')
