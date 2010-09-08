from brameda.contrib import admin
from brameda.crm.models import Contact,Employer

MODULE_INDEX = 1

class CrmAdmin(admin.AppAdmin):

	def render(self):
		self.set('name','Oke')
	

class ContactAdmin(admin.DefaultAdmin):
	position = [MODULE_INDEX,1]
	pass

class EmployerAdmin(admin.DefaultAdmin):
	position = [MODULE_INDEX,0]
	pass

admin.site.register(Contact,ContactAdmin)
admin.site.register(Employer,EmployerAdmin)
