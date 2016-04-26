"""mycms URL Configuration
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from . import settings
from django.contrib import admin
from cms import views
from django.contrib.admin.sites import AdminSite

AdminSite.site_header = settings.SITE_HEADER

urlpatterns = [
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^(?P<slug>[0-9a-z_]+)/$', views.PageView.as_view(), name='page'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
