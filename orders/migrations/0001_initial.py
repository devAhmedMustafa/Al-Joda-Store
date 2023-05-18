# Generated by Django 4.2.1 on 2023-05-18 06:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('purchases', '0013_delete_order'),
        ('users', '0003_alter_shippingdata_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(default='pending', max_length=30)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='purchases.cart')),
                ('ship_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.shippingdata')),
            ],
        ),
    ]
