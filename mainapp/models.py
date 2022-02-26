from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=255, verbose_name='Наименование')
    count = models.PositiveIntegerField(verbose_name='Кол-во на складе')
    price = models.FloatField(verbose_name='Цена')

    def __str__(self):
        return self.name


class CartProduct(models.Model):

    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    count = models.PositiveIntegerField(verbose_name='Количество')

    def cost(self):
        return self.product.price * self.count

    def __str__(self):
        return f'{self.product.name} {self.count}'


class Cart(models.Model):

    user = models.CharField(null=True, max_length=40)
    products = models.ManyToManyField(CartProduct, verbose_name='Товары')
    ordered = models.BooleanField(default=False, verbose_name='В заказе')

    def __str__(self):
        return f'Корзина для {self.user}'

    def get_sum(self):
        return sum([i.cost() for i in self.products.all()])


class Order(models.Model):

    DELIVERY_TYPE = (
        ('SM', 'Самовывоз'),
        ('DL', 'Доставка'),
    )

    cart = models.ForeignKey(Cart, verbose_name='Товары', on_delete=models.CASCADE)
    delivery_type = models.CharField(max_length=255, choices=DELIVERY_TYPE, default='SM', verbose_name='Тип получения')
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    surname = models.CharField(max_length=255, default='', verbose_name='Фамилия')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    address1 = models.CharField(max_length=255, null=True, blank=True, verbose_name='Населенный пункт')
    address2 = models.CharField(max_length=255, null=True, blank=True, verbose_name='Адрес')

    cost = models.PositiveIntegerField(verbose_name='Стоимость', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False, verbose_name='В архиве', null=True, blank=True)

    def __str__(self):
        return f'Заказ для {self.first_name} {self.surname}'
