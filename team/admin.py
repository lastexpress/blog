from django.contrib import admin
from .models import TeamMainTitle, TeamBox
from django.utils.safestring import mark_safe


@admin.register(TeamBox)
class TeamBoxAdmin(admin.ModelAdmin):
	list_display = ('team_name', 'team_tag')
	fields = ['team_img', 'preview', 'team_name', 'team_tag', 'team_url']

	readonly_fields = ['preview']

	def preview(self, obj):
		return mark_safe(f'<img src="{obj.readonly_fields.url}">')

admin.site.register(TeamMainTitle)

