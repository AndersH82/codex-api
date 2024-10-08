from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from .views import APIRootView


urlpatterns = [
    path('', APIRootView.as_view(), name='api-root'),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/admin/login/'), name='login'),
    path('rest-auth/', include('rest_auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(next_page='/admin/login/'), name='logout'),
    path('forum/', include('forum.urls')),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
]