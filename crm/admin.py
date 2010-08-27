from django.contrib import admin

from brameda.crm.models import Contact

class ContactAdmin(admin.ModelAdmin):
	pass

admin.site.register(Contact,ContactAdmin)
