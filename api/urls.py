from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'^sharks/id/(?P<shark_id>[0-9]+)/$', views.SharkByIDView.as_view()),
]