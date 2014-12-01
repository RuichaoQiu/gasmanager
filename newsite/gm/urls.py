from django.conf.urls import patterns, url

from gm import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^test/$', views.TestView.as_view(), name='test'),
    url(r'^addcar/$', views.AddCarView.as_view(), name='addcar'),
    url(r'^(?P<locationzip>\d+)/result/$', views.result, name='result'),
    #url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/editcar/$', views.EditCarView.as_view(), name='editcar'),
    url(r'^recordmanager/$', views.recordmanager, name='recordmanager'),
    
)