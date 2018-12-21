from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    name = models.OneToOneField(User, on_delete=True, related_name='employee', verbose_name='Пользователяь')
    phone = models.CharField(max_length=50, verbose_name='Телефон')

class Food(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название блюда')
    descrption = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Оисание блюда')
    photo = models.ImageField(verbose_name='Фотография')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')

class Order(models.Model):
    STATUS_NEW = 'new'
    STATUS_PREPARING = 'preparing'
    STATUS_ON_WAY = 'on_way'
    STATUS_DELIVERED = 'delivered'
    STATUS_CANCELED = 'canceled'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Новый'),
        (STATUS_PREPARING, 'Готовиться'),
        (STATUS_ON_WAY, 'В пути'),
        (STATUS_DELIVERED, 'Доставка'),
        (STATUS_CANCELED, 'Отменён'),
    )

    contact_phone = models.CharField(max_length=50, verbose_name='Телефон')
    contact_name = models.CharField(max_length=100, verbose_name='Имя клиента')
    delivery_adress = models.CharField(max_length=200, null=True, blank=True, verbose_name='Адрес доставки')
    status = models.CharField(max_length=20, default=STATUS_NEW, verbose_name='Статус', choices=STATUS_CHOICES)
    operator = models.ForeignKey(User, null=True, blank=True, related_name='orders', verbose_name='Оператор', on_delete=models.PROTECT)
    courier = models.ForeignKey(User, null=True, blank=True, related_name='delivered', verbose_name='Курьер', on_delete=models.PROTECT)

class OrderFoods(models.Model):
    order = models.ForeignKey(Order, related_name='foods', on_delete=models.PROTECT, verbose_name='Заказ')
    food = models.ForeignKey(Food, related_name='+', on_delete=models.PROTECT, verbose_name='Блюдо')
    amount = models.IntegerField(verbose_name='Количество')
