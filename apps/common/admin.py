from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from solo.admin import SingletonModelAdmin
from apps.common.models import Common, Footer


@admin.register(Footer)
class FooterAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Common)
class CommonAdmin(SingletonModelAdmin):
    pass
