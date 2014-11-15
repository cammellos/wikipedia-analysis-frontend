from django.conf.urls import url

from edit_history import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
