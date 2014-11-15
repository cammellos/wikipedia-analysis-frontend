from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^edit_history/', include('edit_history.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
