# Generated by Django 4.0.1 on 2022-01-13 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_alter_order_archived_alter_order_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='ordered',
            field=models.BooleanField(default=False, verbose_name='В заказе'),
        ),
    ]
