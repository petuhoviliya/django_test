from django.conf.urls import url

from . import views

app_name='feedback'
urlpatterns = [
	url(r'^$', views.index_view, name='index'),
	url(r'^login/$', views.login_view, name='login'),
	url(r'^logout/$', views.logout_view, name='logout'),
	url(r'^msg/$', views.msg, name='msg'),	
]
	