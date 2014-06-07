from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = patterns('',
	url(r'^$', views.UserList.as_view()),
	url(r'^(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += patterns('',
	url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
)