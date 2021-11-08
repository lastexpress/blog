from django.db import models


class ReloadTitle(models.Model):
	off_title = models.CharField(max_length=50, verbose_name='Main title')

	def __str__(self):
		return self.off_title

	class Meta:
		verbose_name = 'Заголовок'
		verbose_name_plural = 'Заголовки'

class ReloadTitleDesc(models.Model):
	rtd_title = models.CharField(max_length=30, verbose_name='заголовки в карточке')
	rtd_desc = models.TextField(max_length=220, verbose_name='Описание карточки')
	rtd_button = models.CharField(max_length=20, verbose_name='Описание кнопки')

	def __str__(self):
		return self.rtd_title

	class Meta:
		verbose_name = 'Карточка'
		verbose_name_plural = 'Карточки'
