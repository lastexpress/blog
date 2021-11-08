from django.contrib import admin
from .models import Category, Photo
from django.utils.safestring import mark_safe

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
	list_display = ('category', 'gal_title', 'image')

	fields = ('category', 'gal_title', 'image', 'watch_img')

	readonly_fields = ['watch_img']

	def watch_img(self, img):
		return mark_safe(f'<img src="{img.image.url}">')
