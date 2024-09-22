from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, PostViewSet, CommentViewSet, LikeViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]