from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group

from brameda.contrib import admin
from brameda.system.models import Log,LogSummary

MODULE_INDEX = 1000

class LogAdmin(admin.DefaultAdmin):
	position = [MODULE_INDEX,1]

	date_hierarchy = 'datetime'
	model = Log
	list_display = ['datetime_fmt', 'host', 'level', 'source', 'abbrev_msg']
	list_editable = []
	search_fields = ['source', 'msg', 'host']
	list_filter = ['level', 'source', 'host']

class LogSummaryAdmin(admin.DefaultAdmin):
	position = [MODULE_INDEX,2]

	date_hierarchy = 'latest'
	model = LogSummary
	list_display = ['latest_fmt', 'earliest_fmt', 'hits', 'host', 'level', 'source', 'headline', 'abbrev_msg', 'summary_only']
	list_editable = ['summary_only']
	search_fields = ['source', 'latest_msg', 'host']
	list_filter = ['level', 'source', 'host']

admin.site.register(Log,LogAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Group,GroupAdmin)

#admin.site.register(LogSummary,LogSummaryAdmin)
