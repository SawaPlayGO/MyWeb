from django.db import models

class Marmelad_order(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описание')
    auction = models.BooleanField('Торг')
    price = models.DecimalField('Цена за 1 кг', max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Marmelad_order'

    def __str__(self):
        return f'{self.title} {self.description} {self.auction} {self.price} {self.created_at} {self.update_at}'
