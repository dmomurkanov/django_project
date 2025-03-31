from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from solo.admin import SingletonModelAdmin
from common.models import Footer, Common


@admin.register(Footer)
class FooterAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Common)
class CommonAdmin(SingletonModelAdmin):
    pass
