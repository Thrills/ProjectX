from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /paper/
    url(r'^$', views.index, name='index'),
    # ex: /paper/5/
    url(r'^(?P<paper_code>[0-9]+)/$', views.paper, name='paper'),
    # ex: /paper/5/review/
    url(r'^(?P<paper_code>[0-9]+)/review/$', views.review, name='review'),
]
