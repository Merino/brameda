import re

from django.conf import settings
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.text import capfirst

site = admin.site

def applist(request):
	app_dict = {}

	if request.path == '/admin/':
		active = True
	else:
		active = False

	app_dict['Dashboard'] = {
						'name': 'Dashboard',
						'app_url': '/admin/',
						'has_module_perms': True,
						'models':{},
						'position':0,
						'active':active,
					}

	user = request.user
	for model, model_admin in site._registry.items():
		app_label = model._meta.app_label

		
		
		has_module_perms = user.has_module_perms(app_label)
		
		try: 
			position = model_admin.position
		except AttributeError:
			position = [99,99]
	
		if has_module_perms:
			perms = model_admin.get_model_perms(request)
			
			if True in perms.values():

				active = False

				model_url = mark_safe('/admin/%s/%s/' % (app_label, model.__name__.lower()))

				if app_label == 'auth':
					app_label = 'system'

				if re.match(model_url,request.path):
					active = True
				
				model_dict = {
					'name': capfirst(model._meta.verbose_name_plural),
					'admin_url':model_url,
					'perms': perms,
					'position':position[1],
					'active':active,
				}
				if app_label in app_dict:
					
					# TODO sort model on position
					app_dict[app_label]['models'].insert(position[1],model_dict)

					if active:
						app_dict[app_label]['active'] = active

				else:
	
					app_url = mark_safe('/admin/%s/' % (app_label))

					if request.path == app_url:
						active = True

					app_dict[app_label] = {
						'name': app_label.title(),
						'app_url': app_url,
						'has_module_perms': has_module_perms,
						'models': [model_dict],
						'position':position[0],
						'active':active,
					}
					
	app_list = app_dict.values()
	app_list.sort(lambda x, y: cmp(x['position'], y['position']))
	return {'adm_app_list': app_list,'organisation_name':settings.ORGANISATION_NAME}

