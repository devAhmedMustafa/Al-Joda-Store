# Generated by Django 4.2.1 on 2023-05-16 07:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0004_alter_cartitem_cart_alter_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2023, 5, 16, 7, 51, 21, 25651, tzinfo=datetime.timezone.utc)),
        ),
    ]