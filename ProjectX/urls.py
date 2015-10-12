#ProjectX URL Configuration
from django.conf.urls import include, url, patterns
from django.contrib import admin
# from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', 'papers.views.home', name='home'),
    url(r'^about', 'papers.views.about', name='about'),
    url(r'^help', 'papers.views.userdocumentation', name='help'),
    url(r'^success', 'papers.views.success', name='success'),
    url(r'^login/$', 'papers.views.auth_login', name='login'),
    url(r'^logout/$', 'papers.views.auth_logout', name='logout'),
    url(r'^registration', 'papers.views.registration', name='registration'),
    url(r'^review_sub/', 'papers.views.review_sub', name='review_sub'),
    url(r'^paper_sub', 'papers.views.paper_sub', name='paper_sub'),
    url(r'^booking', 'booking.views.booking', name='booking'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # This the url link to the documentation for admin
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')), 
    url(r'^accounts/profile/', TemplateView.as_view(template_name='profile.html'), name='profile')
]
