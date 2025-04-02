from apps.items.models import Category, SubCategory, Item


class TemplateService:

    def get_category(self):
        return Category.objects.all()

    def get_items(self):
        return Item.objects.all

    def get_subcategory(self, category_id):
        return SubCategory.objects.filter(category=category_id)
