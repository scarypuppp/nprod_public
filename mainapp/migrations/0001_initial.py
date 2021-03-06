# Generated by Django 4.0.1 on 2022-01-08 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('measuring', models.CharField(choices=[('KG', 'Килограммы'), ('ED', 'Штучный')], default='ED', max_length=255, verbose_name='Размерность')),
                ('count', models.PositiveIntegerField(verbose_name='Кол-во на складе')),
                ('price', models.FloatField(verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_type', models.CharField(choices=[('DL', 'Доставка'), ('SM', 'Самовывоз')], default='SM', max_length=255, verbose_name='Тип получения')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('phone_number', models.PositiveIntegerField(verbose_name='Номер телефона')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('cost', models.PositiveIntegerField(verbose_name='Стоимость')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('archived', models.BooleanField(default=False, verbose_name='В архиве')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.cart', verbose_name='Товары')),
            ],
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(verbose_name='Количество')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product', verbose_name='Товар')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(to='mainapp.Product', verbose_name='Товары'),
        ),
    ]
