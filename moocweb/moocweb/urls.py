from django.conf.urls import patterns, include, url
from django.contrib import admin
from moocweb import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^moocweb/', include('moocweb.urls')),
    # url(r'^admin/', include(admin.site.urls)),
	# url(r'^test/$', views.test, name='test'),
	# url(r'^search/(?P<keywords>.*)/$', views.search, name='search'),
	url(r'^search$', views.search, name='search'),
)
