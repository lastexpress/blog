from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

#Менеджер для загрузки постов
class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager, self).get_queryset().filter(status='published')

#Категории
class CategoryList(models.Model):
	parent = models.ForeignKey("FmBlog", on_delete=models.SET_NULL, null=True, blank=True)
	category_name = models.CharField(max_length=250, verbose_name='Название категории')
	slug = models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.category_name

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'


#ПОСТЫ
class FmBlog(models.Model):
	STATUS_CHOICES = (
		('close', 'Close'),
		('published', 'Published'),
	)
	category = models.ForeignKey("CategoryList", on_delete=models.CASCADE, null=True, blank=True)
	fm_img = models.ImageField(upload_to='fmblogimg/', null=True, blank=True)
	title = models.CharField(max_length=250, verbose_name='Заголовок блога')
	slug = models.SlugField(max_length=250, unique_for_date='publish')
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
	body = models.TextField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)
	post_btn = models.CharField(max_length=20, verbose_name='Название кнопки', null=True, blank=True)
	status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='published')

	#Менеджер
	objects = models.Manager() #Менеджер по умолчанию
	published = PublishedManager() #Новый менеджер

	#Канонические ссылки
	def get_absolute_url(self):
		return reverse('bloges:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('-publish',)

	tags = TaggableManager()


class Comment(models.Model):
	post = models.ForeignKey(FmBlog, on_delete=models.CASCADE, related_name='comments')
	name = models.CharField(max_length=80)
	email = models.EmailField()
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return f'Comment by {self.name} on {self.post}'

	class Meta:
		ordering = ('created',)




#ИЗменить заголовок категории
class ChangeTitleCategory(models.Model):
	category_title = models.CharField(max_length=250, verbose_name='Название Заголовка')

	def __str__(self):
		return self.category_title

	class Meta:
		verbose_name = 'Заголовок категорий'
		verbose_name_plural = verbose_name


#Заменить заголовок
class ChangeTitle(models.Model):
	change_title = models.CharField(max_length=20, verbose_name='Заголовок блога')

	def __str__(self):
		return self.change_title

	class Meta:
		verbose_name = 'Заголовок'
		verbose_name_plural = 'Заголовки'
