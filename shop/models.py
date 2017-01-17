from django.db import models
from django.contrib.contenttypes import fields
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


# Create your models here.


class Good(models.Model):
	name = models.CharField(verbose_name = 'Наименование', null=True, blank=True, max_length = 200)
	category = models.CharField(verbose_name = 'Категория', null=True, blank=True, max_length = 200)
	cost = models.BigIntegerField(verbose_name = 'Цена', null=True, blank=True)
	description = models.TextField(verbose_name = 'Описание', null=True, blank=True)
	preview = models.ImageField(upload_to="images/", null=True, blank=True)
	warhouse = models.IntegerField(verbose_name = 'Наличие', null=True, blank=True)

	class Meta:
		verbose_name = u'Товар'
		verbose_name_plural = u'Товары'

	def __str__(self):
		return self.name 
		ordering = ["-id"]

class GoodImage(models.Model):
	img = models.ImageField(upload_to="images/", null=True, blank=True)
	parent = models.ForeignKey(Good, null=True, blank=True)

	class Meta:
		verbose_name = u'Фото товара'
		verbose_name_plural = u'Фото товара'

	def __str__(self):
		return u'Image # ' + str(self.id) 

class GoodApp(models.Model):
	parent_good = models.ForeignKey(Good, null=True, blank=True)
	parent_user = models.ForeignKey(User, null=True, blank=True)

	COUNTRY_CHOICES = (
		("Россия", 'Россия'),
		("Белоруссияя", 'Белоруссия'),
		("Азербайджан", 'Азербайджан'),
		("Казахстан", 'Казахстан'),
		("Армения", 'Армения'),
	)
	count = models.IntegerField(verbose_name = 'Количество заказываемого товара', null=True)
	country = models.CharField(verbose_name = 'Страна', null=True, max_length = 200, choices = COUNTRY_CHOICES)
	district = models.CharField(verbose_name = 'Область', null=True, max_length = 200)
	town = models.CharField(verbose_name = 'Город', null=True, max_length = 200)
	addres = models.CharField(verbose_name = 'Адрес улицы/дома', null=True, max_length = 200)

	#contacts

	email = models.EmailField(verbose_name = 'E-mail', null=True, blank=True, max_length = 200)
	phone = models.CharField(verbose_name = 'Контактный телефон', null=True, blank=True, max_length = 200)

	class Meta:
		verbose_name = u'Заказ'
		verbose_name_plural = u'Заказы'

	def __str__(self):
		return u'Заказ # ' + str(self.id)
