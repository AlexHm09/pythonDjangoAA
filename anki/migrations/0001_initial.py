# Generated by Django 4.2.13 on 2024-05-18 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnkiCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_cards', models.CharField(max_length=50, verbose_name='Название карточки')),
                ('description', models.TextField(verbose_name='Описание карточки')),
            ],
        ),
    ]
