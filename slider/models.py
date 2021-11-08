from django.db import models

class Slider(models.Model):
	slider_img = models.ImageField(upload_to='sliderimg/')
	slider_title = models.CharField(max_length=200, verbose_name='Заголовок')
	slider_css = models.CharField(max_length=200, null=True, default='-', verbose_name='css class')

	def __str__(self):
		return self.slider_title

	class Meta:
		verbose_name = 'Слайд'
		verbose_name_plural = 'Слайды'