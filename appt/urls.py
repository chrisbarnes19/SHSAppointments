from django.conf.urls import url
from django.contrib.auth.views import login, logout


from . import views


urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^register/$', views.register, name = 'register'),
	url(r'^login/$', views.user_login, name = 'login'),
	url(r'^logout/$', views.user_logout, name ='logout'),
	url(r'^(?P<pk>[0-9]+)/$', views.new_appointment, name='new_appointment'),
	url(r'^appointments/(?P<month>[0-9]+)/(?P<day>[0-9]+)/(?P<year>[0-9]+)/$', views.date_view, name='date_view'),
	url(r'^confirmation/(?P<pk>[0-9]+)/$', views.confirmation, name='confirmation'),
	url(r'^monthly/$' views.monthly_view, name = 'monthly_view'),
]