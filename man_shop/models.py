from django.db import models

class Man_shop(models.Model):
    SIZE_P = (
        ('L', 'L'),
        ('M', 'M'),
        ('X', 'X'),
        ('XL', 'XL')
    )

    COMPOUND_P = (
        ('Хлопок', 'Хлопок'),
        ('Синтетика', 'Синтетика'),
        ('Шерсть', 'Шерсть')
    )

    SHAPE_P = (
        ('Новая', 'Новая'),
        ('Б/У', 'Б/У')
    )

    product_name = models.CharField('Название товара:', max_length=100)
    image = models.ImageField('Фото товара', upload_to='')
    size = models.CharField('Размер этого товара:', default='L', choices=SIZE_P, max_length=10, null=True)
    compound = models.CharField('Состав:', max_length=100, choices=COMPOUND_P, blank=True)
    color = models.CharField('Цвет товара:', max_length=50, null=True)
    made_in = models.CharField('Где сделан это товар:', max_length=100, blank=True)
    price = models.PositiveIntegerField('Цена товара:')
    shape = models.CharField('Состояние товара:', max_length=100, choices=SHAPE_P)

    def __str__(self):
        return self.product_name


    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'





