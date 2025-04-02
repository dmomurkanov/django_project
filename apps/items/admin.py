from django.contrib import admin
from django.contrib.admin import TabularInline
from adminsortable2.admin import SortableAdminMixin
from modeltranslation.admin import TabbedTranslationAdmin


from .models import Item, Category, SubCategory, Characteristic, Cart, CartItem


# @admin.register(Characteristic)
class CharacteristicInline(TabularInline):
    model = Characteristic


@admin.register(Item)
class ItemAdmin(SortableAdminMixin, TabbedTranslationAdmin):
    inlines = [CharacteristicInline, ]


@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, TabbedTranslationAdmin):
    pass


@admin.register(SubCategory)
class Subcategory(SortableAdminMixin, admin.ModelAdmin):
    pass


class CardItemInline(admin.TabularInline):
    model = CartItem
    extra = 0


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CardItemInline, ]


