from django.db import models


class Deal(models.Model):
    """Сделки"""
    customer = models.CharField('Никнэйм покупателя', max_length=100)
    item = models.CharField('Название товара', max_length=100)
    total = models.IntegerField('Потраченная сумма сделки', default=0)
    quantity = models.IntegerField('Кол-во товара', default=0)
    date = models.DateTimeField('Дата сделки', auto_now_add=True)

