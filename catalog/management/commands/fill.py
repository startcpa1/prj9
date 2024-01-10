import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        category_for_create = []

        with open('data.json', encoding='utf-8') as f:
            category_list = json.load(f)
            for category_item in category_list:
                category_for_create.append(Category(**category_item['fields']))


        Category.objects.bulk_create(category_for_create)

