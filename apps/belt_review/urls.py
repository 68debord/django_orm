from django.conf.urls import url


from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^register/$', views.register),
	url(r'^login/$', views.login),
	url(r'^books/$', views.books),
	url(r'^books/add/$', views.add),
	url(r'^books/add/process/$', views.dualprocess),
	url(r'^books/(?P<id>\d+)/$', views.bookshow),
	url(r'^books/(?P<id>\d+)/process/$', views.singleprocess),
	url(r'^review/(?P<id>\d+)/delete/$', views.delete),
	url(r'^users/(?P<id>\d+)/$', views.user),
	url(r'^logout/$', views.logout),
]
