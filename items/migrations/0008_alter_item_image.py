# Generated by Django 5.1.7 on 2025-03-14 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_item_sub_category_alter_subcategory_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(null=True, upload_to='tovar', verbose_name='Главная картинка товара'),
        ),
    ]
