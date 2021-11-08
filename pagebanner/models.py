from django.db import models


class PageBanner(models.Model):
	banner_name = models.CharField(max_length=250, verbose_name='Название главного заголовка')
	banner_btn_1 = models.CharField(max_length=250, verbose_name='Название первого раздела')
	banner_btn_2 = models.CharField(max_length=250, verbose_name='Название второго раздела')
	banner_btn_3 = models.CharField(max_length=250, verbose_name='Название третьего раздела')

	def __str__(self):
		return self.banner_name

	class Meta:
		verbose_name = 'Заголовок баннера'
		verbose_name_plural = verbose_name