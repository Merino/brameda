from django.template import RequestContext
from django.contrib import admin
from django.shortcuts import render_to_response

class ErpAdmin(admin.AdminSite):
	
	def index(self,request,extra_context=None):

		return super(ErpAdmin,self).index(request,extra_context)

	def get_urls(self):

		from django.conf.urls.defaults import patterns,url,include

		urlpatterns = super(ErpAdmin,self).get_urls()
		
		urlpatterns = patterns('',url(r'^crm/$','brameda.crm.admin.CrmAdmin')) + urlpatterns

		return urlpatterns
	
class AppAdmin(object):
	
	template = 'admin/app_index.html'
	var = {}

	def __new__(cls,request,*args, **kwargs):
		view = cls.new(request, *args, **kwargs)
		
		view.render()

		return view.create_response()

	# TODO Make Function
	def set(self,name,data):
		pass

	@classmethod
	def new(cls,*args,**kwargs):
		obj = object.__new__(cls)
		obj.__init__(*args,**kwargs)

		return obj

	def __init__(self,request,*args,**kwargs):
		self.request = request

	def render(self):
		raise NotImlementedError()

	def create_response(self):

		context_instance = RequestContext(self.request)

		return render_to_response(self.template,self.var,context_instance=context_instance)


class DefaultAdmin(admin.ModelAdmin):
	position = False

	def get_position(self):
		return self.position

site = ErpAdmin()
