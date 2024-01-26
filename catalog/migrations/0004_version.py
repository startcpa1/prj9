# Generated by Django 5.0.1 on 2024-01-26 19:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_product_createdate_alter_product_lastdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1, verbose_name='Номер')),
                ('name', models.CharField(default='Создана', max_length=100, verbose_name='Название')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активная')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Версия',
                'verbose_name_plural': 'Версии',
            },
        ),
    ]
