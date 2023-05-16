# Generated by Django 4.2.1 on 2023-05-16 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=999)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField(blank=True, null=True)),
                ('type_book', models.TextField()),
                ('genre', models.CharField(choices=[('DETECTIVE', 'DETECTIVE'), ('ROMANS', 'ROMANS')], max_length=200)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]