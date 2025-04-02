from django.core.management import BaseCommand

from apps.items.models import Item

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # sub_category = SubCategory.objects.get(id=2)
        # item = Item.objects.create(
        #     sub_category=sub_category,
        #     image="C:/Users/NB-8/PycharmProjects/MegaDjango/items/img_box/quest-bunker/jpg",
        #     title="qwertyuio",
        #     description="qwertyu",
        #     price=14456.00,
        #     production="apple",
        #     model="iphone16",
        #     is_available=True,
        #     color="blue",
        #
        # item.save()
        items = Item.objects.filter(is_available=True, title="iphone")
        print(items)
        for item in items:
            item.is_available = False
            item.save(update_fields=["is_available",])
