from django.contrib import admin

from brameda.system.admin import DefaultAdmin
from brameda.crm.models import Contact,Employer

MODULE_INDEX = 1

class ContactAdmin(DefaultAdmin):
	position = [MODULE_INDEX,1]


class EmployerAdmin(DefaultAdmin):
	position = [MODULE_INDEX,0]

admin.site.register(Contact,ContactAdmin)
admin.site.register(Employer,EmployerAdmin)
