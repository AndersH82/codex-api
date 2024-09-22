from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


class CustomLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'


class APIRootView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            'profiles': reverse('profile-list', request=request, format=format),
            'posts': reverse('post-list', request=request, format=format),
            'comments': reverse('comment-list', request=request, format=format),
            'likes': reverse('like-list', request=request, format=format),
        })