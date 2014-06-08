from django.conf.urls import patterns, url
from questions import views

urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>\d+)/$', views.QuestionView.as_view(), name='question'),
	url(r'^(?P<ques_id>\d+)/save/$', views.saveAnswer, name='saveAnswer'),
)