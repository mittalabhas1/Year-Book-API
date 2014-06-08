from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'YearBookAPI.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
	url(r'^auth-token/', 'rest_framework_jwt.views.obtain_jwt_token'),
	url(r'^users/', include('users.urls')),
	url(r'^question/', include('questions.urls')),
)