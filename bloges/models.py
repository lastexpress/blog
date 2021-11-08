from django.db import models
from phonenumber_field.modelfields import PhoneNumberField




class ChangeHeader(models.Model):
	header_name = models.CharField(max_length=15, verbose_name='Название модели')
	header_single_letter = models.CharField(max_length=1, verbose_name='Заглавная буква лого')
	header_logo_text = models.CharField(max_length=20, verbose_name='Текст букв лого')
	header_main = models.CharField(max_length=250, verbose_name='Название меню')
	header_features = models.CharField(max_length=250, verbose_name='Название 2 блока')
	header_work = models.CharField(max_length=250, verbose_name='Название 3 блока')
	header_service = models.CharField(max_length=250, verbose_name='Название 4 блока')
	header_blog = models.CharField(max_length=250, verbose_name='Название 5 блока')
	header_price = models.CharField(max_length=250, verbose_name='Название 6 блока')
	header_about = models.CharField(max_length=250, verbose_name='Название 7 блока')
	header_contact = models.CharField(max_length=250, verbose_name='Название 7 блока')
	header_phone = PhoneNumberField(null=False, blank=False, unique=True)

	def __str__(self):
		return self.header_name

	class Meta:
		verbose_name = 'Header'
		verbose_name_plural = verbose_name


class ChangeFooter(models.Model):
	footer_logo_img = models.ImageField(upload_to='footerimg/')
	footer_title = models.TextField()
	footer_facebook = models.CharField(max_length=250, verbose_name='Ссылка на фейсбук')
	footer_twitter = models.CharField(max_length=250, verbose_name='Ссылка на твиттер')
	footer_in = models.CharField(max_length=250, verbose_name='Ссылка на in')
	footer_telegram = models.CharField(max_length=250, verbose_name='Ссылка на telegram')
	footer_vimeo = models.CharField(max_length=250, verbose_name='Ссылка на vimeo')
	footer_pictures = models.CharField(max_length=250, verbose_name='Ссылка на pictures')
	footer_left_title = models.CharField(max_length=250, verbose_name='Заголовок (слева) контакт')
	footer_left_map = models.CharField(max_length=250, verbose_name='Контакт Адрес')
	footer_left_email = models.CharField(max_length=250, verbose_name='Контакт почты')
	footer_center_title = models.CharField(max_length=250, verbose_name='Заголовок center')
	footer_center_desc = models.CharField(max_length=250, verbose_name='Описание работы')
	footer_center_work = models.CharField(max_length=250, verbose_name='MON - FRI : 9.00 AM TO 5.00 PM')
	footer_center_work1 = models.CharField(max_length=250, verbose_name='SAT - SUN : 11.00 AM TO 3.00 PM')

	def __str__(self):
		return self.footer_title

	class Meta:
		verbose_name = 'Footer'
		verbose_name_plural = verbose_name


class ChangeFooterTitleGallery(models.Model):
	footer_right_title = models.CharField(max_length=250, verbose_name='Заголовок справа')

	def __str__(self):
		return self.footer_right_title

	class Meta:
		verbose_name = 'Заголовок справа'
		verbose_name_plural = verbose_name


class ChangeFooterGallery(models.Model):
	footer_right_name = models.CharField(max_length=250, verbose_name='Название картинки', default='this stroke')
	footer_right_img = models.ImageField(upload_to='footerimg/')

	def __str__(self):
		return self.footer_right_name

	class Meta:
		verbose_name = 'Картинка'
		verbose_name_plural = 'Картинки'
