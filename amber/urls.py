from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from persistence.api.v1 import amber_api as amber_api_v1

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(amber_api_v1.urls)),
)
