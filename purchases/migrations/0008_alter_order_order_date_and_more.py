# Generated by Django 4.2.1 on 2023-05-16 08:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_on_stock_product_in_stock'),
        ('purchases', '0007_alter_cart_user_alter_cartitem_cart_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2023, 5, 16, 8, 3, 31, 588289, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('product', 'cart')},
        ),
    ]
