from django.db import models



class BuildWebsite(models.Model):
	bw_title = models.CharField(max_length=50, verbose_name='Заголовок bws')
	bw_desc = models.TextField()

	def __str__(self):
		return self.bw_title

	class Meta:
		verbose_name = 'BuildWs'
		verbose_name_plural = verbose_name

class BuildButton(models.Model):
	bb_btn = models.CharField(max_length=25, verbose_name='Кнопка')

	def __str__(self):
		return self.bb_btn

	class Meta:
		verbose_name = 'Кнопка'
		verbose_name_plural = 'Кнопки'

class MainImage(models.Model):
	main_title = models.CharField(max_length=20, verbose_name='Название картинки')
	main_img = models.ImageField(upload_to='BuildWs')

	def __str__(self):
		return self.main_title

	class Meta:
		verbose_name = 'Картинка'
		verbose_name_plural = 'Картинки'
