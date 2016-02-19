from django.conf.urls import url

from . import views

app_name = 'tracker'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^students$', views.students, name='students'),
	url(r'^(?P<last_name>\w+)-(?P<first_name>\w+)/$', views.detail, name='detail'),
]