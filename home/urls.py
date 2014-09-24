from django.conf.urls import patterns, url

urlpatterns = patterns('home.views',
                        url(r'^post_save/$','user_register'),
                        url(r'^Display_post/$','Display_post'),
                        url(r'^reply_save/(?P<id>.*)$', 'save_reply'),
                       )
