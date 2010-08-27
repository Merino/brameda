import os
import sys

apache = os.path.dirname(__file__)
project= os.path.dirname(apache)
workspace=os.path.dirname(project)

sys.path.insert(0,workspace)

os.environ['DJANGO_SETTINGS_MODULE'] = 'brameda.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
