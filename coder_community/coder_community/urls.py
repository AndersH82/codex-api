from django.urls import path
from django.contrib import admin
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/admin/login/'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/admin/login/'), name='logout'),
]