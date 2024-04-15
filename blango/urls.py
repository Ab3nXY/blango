import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
import blog.views
import blango_auth.views
from django_registration.backends.activation.views import RegistrationView
from blango_auth.forms import BlangoRegistrationForm
from django.conf.urls.static import static
from django.urls import re_path
from  django.views.static import serve
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", blog.views.index, name="index"),
    path("post/<slug>/", blog.views.post_detail, name="blog-post-detail"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("allauth.urls")),
    path("accounts/profile/", blango_auth.views.profile, name="profile"),
    path(
    "accounts/register/",
    RegistrationView.as_view(form_class=BlangoRegistrationForm),
    name="django_registration_register",
),
    path("accounts/", include("django_registration.backends.activation.urls")),
    path("api/v1/", include("blog.api.urls")),
    path("post-table/", blog.views.post_table, name="blog-post-table"),
    path("create_blog/", blog.views.create_blog, name="create_blog"),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),



]

# Serve static and media files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 