"""ProjectX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
# from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', 'papers.views.home', name='home'),
    url(r'^registration', 'papers.views.registration', name='registration'),
    # url(r'^cm_reg', 'papers.views.cm_reg', name='cm_reg'),
    # url(r'^reviewer_reg', 'papers.views.reviewer_reg', name='reviewer_reg'),
    # url(r'^author_reg', 'papers.views.author_reg', name='author_reg'),
    url(r'^booking/', include('booking.urls', namespace="booking")),
    url(r'^papers/', include('papers.urls', namespace="papers")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')), 
    # Django-Registration-Redux
]
