from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, feed

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('feed/', feed, name='feed'),
]

urlpatterns += router.urls
router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = router.urls
