from django.contrib import admin
from .models import FmBlog, Comment, ChangeTitle, ChangeTitleCategory, CategoryList
from django.utils.safestring import mark_safe

@admin.register(FmBlog)
class FmBlogAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'publish', 'status', 'fm_img')
	list_filter = ('status', 'created', 'publish', 'status')
	search_fields = ('title', 'body')
	prepopulated_fields = {'slug' : ('title',)}
	raw_id_fields = ('author',)
	date_hierarchy = 'publish'
	ordering = ('status', 'publish')

	fields = ['category', 'fm_img', 'preview', 'title', 'slug', 'author', 
									'body', 'publish', 'post_btn', 'status']

	readonly_fields = ['preview']

	def preview(self, obj):
		return mark_safe(f'<img src="{obj.fm_img.url}">')

admin.site.register(ChangeTitle)
admin.site.register(ChangeTitleCategory)
admin.site.register(CategoryList)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'post', 'created', 'active')
	list_filter = ('active', 'created', 'updated')
	search_fields = ('name', 'email', 'body')