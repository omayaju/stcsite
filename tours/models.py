from django.db import models
from django.contrib.contenttypes import fields
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


# Create your models here.

class Tour(models.Model):
	name = models.CharField(verbose_name = 'Название', max_length = 200, null=True, blank=True)
	destination = models.CharField(verbose_name = 'Место', max_length = 200, null=True, blank=True)
	description = models.TextField(verbose_name = 'Описание', null=True, blank=True)
	start_date = models.DateField(verbose_name = 'Дата начала', null=True, blank=True)
	finish_date = models.DateField(verbose_name = 'Дата конца', null=True, blank=True)
	hotel = models.CharField(verbose_name = 'Отель/гостиница', max_length = 200, null=True, blank=True)
	main_img = models.ImageField(upload_to="images/", null=True, blank=True)
	tagline = models.CharField(verbose_name = 'Тэг', max_length = 200, null=True, blank=True)
	cost = models.BigIntegerField(verbose_name = 'Стоимость', null=True, blank=True)
	sell = models.IntegerField(verbose_name = 'Процент сезонной скидки', null=True, blank=True)
	food = models.CharField(verbose_name = 'Питание', null=True, blank=True, max_length = 200)
	places = models.IntegerField(verbose_name = 'Свободные места', null=True, blank=True)
	hotel_addres = models.CharField(verbose_name = 'Адрес отеля', max_length = 200, null=True, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = u'Тур'
		verbose_name_plural = u'Туры'
		ordering = ["-start_date"]

class Room(models.Model):
	name = models.CharField(verbose_name = 'Название', max_length = 200, null=True, blank=True)
	description = models.CharField(verbose_name = 'Описание', max_length = 200, null=True, blank=True)
	parent = models.ForeignKey(Tour, null=True, blank=True)
	cost = models.BigIntegerField(verbose_name = 'Стоимость', null=True, blank=True)

	class Meta:
		verbose_name = u'Номер'
		verbose_name_plural = u'Номера'
		ordering = ["-id"]

class Image(models.Model):
	img = models.ImageField(upload_to="images/", null=True, blank=True)
	parent = models.ForeignKey(Tour, null=True, blank=True)

	class Meta:
		verbose_name = u'Фото'
		verbose_name_plural = u'Фото'

	def __str__(self):
		return u'Image # ' + str(self.id) 

class Review(models.Model):
	text = models.CharField(verbose_name = 'Текст', null=True, blank=True, max_length = 500)
	date = models.DateTimeField(verbose_name = 'Дата публикации', null=True, blank=True)
	parent_tour = models.ForeignKey(Tour, null=True, blank=True)
	parent_user = models.ForeignKey(User, null=True, blank=True)

	class Meta:
		verbose_name = u'Отзыв'
		verbose_name_plural = u'Отзывы'
		ordering = ["-date"]

	def __str__(self):
		return u'Отзыв # ' + str(self.id)

class App(models.Model):
	parent_tour = models.ForeignKey(Tour, null=True, blank=True)
	parent_user = models.ForeignKey(User, null=True, blank=True)

	COUNTRY_CHOICES = (
		("Россия", 'Россия'),
		("Белоруссияя", 'Белоруссия'),
		("Азербайджан", 'Азербайджан'),
		("Казахстан", 'Казахстан'),
		("Армения", 'Армения'),
	)

	#addres

	country = models.CharField(verbose_name = 'Страна', null=True, max_length = 200, choices = COUNTRY_CHOICES)
	district = models.CharField(verbose_name = 'Область', null=True, max_length = 200)
	town = models.CharField(verbose_name = 'Город', null=True, max_length = 200)
	addres = models.CharField(verbose_name = 'Адрес улицы/дома', null=True, max_length = 200)

	#contacts

	email = models.EmailField(verbose_name = 'E-mail', null=True, blank=True, max_length = 200)
	phone = models.CharField(verbose_name = 'Контактный телефон', null=True, blank=True, max_length = 200)

	class Meta:
		verbose_name = u'Заявка'
		verbose_name_plural = u'Заявки'

	def __str__(self):
		return u'Заявка # ' + str(self.id)


class Bgimg(models.Model):
	img = models.ImageField(upload_to="images/", null=True, blank=True)

	class Meta:
		verbose_name = u'Фоновое изображение'
		verbose_name_plural = u'Фоновые изображения'

class Quote(models.Model):
	text = models.TextField(verbose_name = 'Текст цитаты', null=True, blank=True)

	class Meta:
		verbose_name = u'Случайная цитата'
		verbose_name_plural = u'Случайные цитаты'

	def __str__(self):
		return self.text[:50] + '...'
