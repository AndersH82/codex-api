from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, PostViewSet, CommentViewSet, LikeViewSet, PostListView

# Initialize the DefaultRouter
router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)

# Define the urlpatterns
urlpatterns = [
    path('', include(router.urls)),
    path('posts/', PostListView.as_view(), name='post-list'),
]