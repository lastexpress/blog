from django.db import models



class TeamMainTitle(models.Model):
	team_title = models.CharField(max_length=30, verbose_name='Название заголовка')

	def __str__(self):
		return self.team_title

	class Meta:
		verbose_name = 'Заголовок'
		verbose_name_plural = verbose_name


class TeamBox(models.Model):
	team_img = models.ImageField(upload_to='teamimg/')
	team_name = models.CharField(max_length=80, verbose_name='Имя человека')
	team_tag = models.CharField(max_length=20, verbose_name='Специальность')
	team_url = models.CharField(max_length=250, verbose_name='Ссылка на страницу', null=True, blank=True)

	def __str__(self):
		return self.team_name

	class Meta:
		verbose_name = 'Человек'
		verbose_name_plural = verbose_name