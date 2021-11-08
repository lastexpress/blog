from django.db import models

class Features(models.Model):
	fts_title = models.CharField(max_length=200, verbose_name='Заголовок')
	fts_desc = models.TextField(max_length=120, verbose_name='Описание')
	fts_img = models.ImageField(upload_to='sliderimg/', blank=True)

	def __str__(self):
		return self.fts_title

	class Meta:
		verbose_name = 'Функция'
		verbose_name_plural = 'Функции'
