# Generated by Django 4.2.1 on 2023-05-11 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_brand_product_discount_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='on_stock',
        ),
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(default=True),
        ),
    ]
