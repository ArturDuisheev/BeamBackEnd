from django.db import models

from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


class Category(models.Model):
    name = models.CharField(
        _('Наименование категории'),
        max_length=120
    )

    def __str__(self) -> str:
        return f'Категория: {self.name}'
    
    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

class Item(BaseModel):
    product = models.CharField(
        _('Наименование товара'),
        max_length=120
    )
    quantity = models.PositiveIntegerField(
        _('Кол-во')
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='item_category', 
        blank=True, null=True,
        verbose_name=_('Категория')
    )
    # distributor = models.ForeignKey(
    #     'distributor.Distributor',
    #      on_delete=models.PROTECT,
    #      related_name='distributor_item',
    #      verbose_name='Дистрибутор',

    #                                 )

    def __str__(self) -> str:
        return f'товар: {self.product}, кол-во {self.quantity}'
    
    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')

