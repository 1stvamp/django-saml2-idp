# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

try:
    # Django <1.6
    from django.conf.urls.defaults import *
except ImportError:
    from django.conf.urls import *

urlpatterns = patterns('',
    # Example:
    # (r'^idptest/', include('idptest.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # Required for login:
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),

    # URLs for the IDP:
    (r'^idp/', include('saml2idp.urls')),
)
