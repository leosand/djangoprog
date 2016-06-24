from django.conf.urls import patterns, url
urlpatterns = patterns('',
url(r'^accueil/$', 'blog.views.home'),
)