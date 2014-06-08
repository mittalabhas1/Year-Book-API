from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from questions import views

urlpatterns = patterns('',
	url(r'^$', views.QuestionList.as_view()),
	url(r'^(?P<pk>\d+)/$', views.QuestionDetail.as_view()),
	url(r'^(?P<pk>\d+)/user/(?P<uid>\d+)$', views.AnswerView.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)