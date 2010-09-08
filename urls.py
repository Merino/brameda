from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin as discover
from brameda.contrib import admin

discover.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^bramedaerp/', include('bramedaerp.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	(r'^admin/', include(admin.site.urls)),
)
