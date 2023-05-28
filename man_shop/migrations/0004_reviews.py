# Generated by Django 4.2.1 on 2023-05-25 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('man_shop', '0003_alter_man_shop_options_alter_man_shop_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Отзывы на товар:')),
                ('created_add', models.DateTimeField(auto_now_add=True)),
                ('name_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_object', to='man_shop.man_shop')),
            ],
        ),
    ]
