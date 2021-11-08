from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
	"""-------------КАТЕГОРИИ--------------"""
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	name = models.CharField(max_length=50, verbose_name='Заголовок категории', null=False, blank=False)
	slug = models.SlugField(unique=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'категория'
		verbose_name_plural = 'Категории'

class Photo(models.Model):
	"""-------------ФОТО ГАЛЕРЕИ--------------"""
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
	gal_title = models.CharField(max_length=20,verbose_name='Название картинки')
	image = models.ImageField(upload_to='galleryimg/')

	def __str__(self):
		return self.gal_title

	class Meta:
		verbose_name = 'Фотография'
		verbose_name_plural = 'Фотографии'
		