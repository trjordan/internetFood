from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^internetFood/', include('internetFood.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^recipes/$', 'internetFood.recipe.views.index'),
    (r'^recipes/(?P<recipe_id>\d+)/$', 'internetFood.recipe.views.detail'),
    (r'^admin/(.*)', admin.site.root),

)
