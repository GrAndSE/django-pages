'''Url mapping for pages
'''
try:  # Older django versions
    from django.conf.urls.defaults import patterns, url
except:  # Newer django versions
    from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url('^(?P<slug>[\w\d\-]+)/$', views.page_view, name='show_page'),
    url('^(?P<slug>[\w\d\-]+)$', views.page_view, name='show_page'),
    url('^$', views.page_view, name='show_page'),
)
