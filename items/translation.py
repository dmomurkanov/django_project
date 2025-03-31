from modeltranslation import translator

from items.models import Category, Item


@translator.register(Category)
class CategoryTranslations(translator.TranslationOptions):
    fields = ("name",)


@translator.register(Item)
class CategoryTranslations(translator.TranslationOptions):
    fields = (
        'image',
        'title',
        'description',
        'price',
        'production',
        'model',
        'is_available',
        'color',
    )