# Generated by Django 5.1.7 on 2025-03-14 03:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_category_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sub_category', to='items.category'),
        ),
    ]
