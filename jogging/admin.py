from django.contrib import admin
from jogging.models import Log, LogSummary

class LogAdmin(admin.ModelAdmin):
    date_hierarchy = 'datetime'
    model = Log
    list_display = ['datetime_fmt', 'host', 'level', 'source', 'abbrev_msg']
    list_editable = []
    search_fields = ['source', 'msg', 'host']
    list_filter = ['level', 'source', 'host']

class LogSummaryAdmin(admin.ModelAdmin):
    date_hierarchy = 'latest'
    model = LogSummary
    list_display = ['latest_fmt', 'earliest_fmt', 'hits', 'host', 'level', 'source', 'headline', 'abbrev_msg', 'summary_only']
    list_editable = ['summary_only']
    search_fields = ['source', 'latest_msg', 'host']
    list_filter = ['level', 'source', 'host']

admin.site.register(Log, LogAdmin)
admin.site.register(LogSummary, LogSummaryAdmin)
