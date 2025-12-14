from django.urls import path
from .views import RegisterView, LoginView, ProfileView
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from .views import FollowUserView, UnfollowUserView

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('follow/<int:pk>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:pk>/', UnfollowUserView.as_view(), name='unfollow-user'),
]
