# Generated by Django 3.2.24 on 2024-03-09 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(choices=[(2, 'ORDER_PROCESSED'), (3, 'ORDER_DELIVERED'), (4, 'ORDER_REJECTED'), (3, 'ORDER_DELIVERED')], default=0),
        ),
    ]
