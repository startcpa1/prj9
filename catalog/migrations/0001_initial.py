# Generated by Django 5.0.1 on 2024-01-08 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='catalog/')),
                ('category', models.CharField(max_length=100, verbose_name='Категория')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('date', models.DateField(verbose_name='Дата')),
            ],
        ),
    ]