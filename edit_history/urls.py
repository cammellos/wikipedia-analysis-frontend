from django.conf.urls import url

from edit_history import views


urlpatterns = [
    url(r'^urls$', views.method_splitter, {'GET':  views.index, 'POST': views.create}),
    url(r'^urls/new$', views.method_splitter, {'GET':  views.new, 'POST': views.create}),
]
