import os
import sys

apache = os.path.dirname(__file__)
project= os.path.dirname(apache)

sys.path.insert(0,project)

os.environ['DJANGO_SETTINGS_MODULE'] = 'setting'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
