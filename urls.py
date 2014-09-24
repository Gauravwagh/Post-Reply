from django.conf.urls  import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from settings import OUR_APPS,SITE_ROOT,os

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wpl.views.home', name='home'),
    # url(r'^wpl/', include('wpl.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^accounts/', include('registration.backends.default.urls')),
)
urlpatterns += patterns('home.views',url(r'^$', 'user_register'),)

for app in OUR_APPS:
    urlpatterns += patterns('',url(r'^'+app+'/', include(app+'.urls',app_name=app)),)
    


urlpatterns += patterns('',
                        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(SITE_ROOT, 'templates/media')}),
                    )
