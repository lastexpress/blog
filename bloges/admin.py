from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import ChangeHeader, ChangeFooter, ChangeFooterTitleGallery, ChangeFooterGallery

admin.site.register(ChangeHeader)
admin.site.register(ChangeFooter)
admin.site.register(ChangeFooterTitleGallery)

@admin.register(ChangeFooterGallery)
class ChangeFooterGalleryAdmin(admin.ModelAdmin):
	list_display = ['footer_right_name', 'prew']
	fields = ('footer_right_name', 'footer_right_img', 'prew')

	readonly_fields =['prew']

	def prew(self, object):
		return mark_safe(f'<img src="{object.footer_right_img.url}">')