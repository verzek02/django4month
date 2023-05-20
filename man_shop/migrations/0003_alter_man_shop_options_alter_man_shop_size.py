# Generated by Django 4.2.1 on 2023-05-20 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('man_shop', '0002_alter_man_shop_color'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='man_shop',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterField(
            model_name='man_shop',
            name='size',
            field=models.CharField(choices=[('L', 'L'), ('M', 'M'), ('X', 'X'), ('XL', 'XL')], default='L', max_length=10, null=True, verbose_name='Размер этого товара:'),
        ),
    ]