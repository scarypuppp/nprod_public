# Generated by Django 4.0.1 on 2022-01-13 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_alter_order_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='archived',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='В архиве'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cost',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Стоимость'),
        ),
    ]
