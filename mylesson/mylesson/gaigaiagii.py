from django.conf.urls import patterns, include, url

from django.contrib import admin
from mytest import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mylesson.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^Book/$', views.library),
    url(r'^xxx/', views.xxx),
    
)
好烦做实验，做好几遍
