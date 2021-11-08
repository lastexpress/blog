from django.db import models


class PriceChangedTitle(models.Model):
	pc_title = models.CharField(max_length=20, verbose_name='Заголовок цен')

	def __str__(self):
		return self.pc_title

	class Meta:
		verbose_name = 'Заголовок'
		verbose_name_plural = verbose_name


class PriceChanged(models.Model):
	price_title = models.CharField(max_length=20, verbose_name='Название заголовка')
	price_title_desc = models.CharField(max_length=50, verbose_name='Название подзаголовка')
	price_money = models.CharField(max_length=10, verbose_name='Цена')
	price_text_1 = models.CharField(max_length=50, verbose_name='Название первого текста')
	price_text_2 = models.CharField(max_length=50, verbose_name='Название второго текста')
	price_text_3 = models.CharField(max_length=50, verbose_name='Название третьего текста')
	price_text_4 = models.CharField(max_length=50, verbose_name='Название четвёртого текста')
	price_text_5 = models.CharField(max_length=50, verbose_name='Название пятого текста')
	price_btn = models.CharField(max_length=20, verbose_name='Название кнопки')

	def __str__(self):
		return self.price_title

	class Meta:
		verbose_name = 'Цена'
		verbose_name_plural = 'Цены'
