from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import User as CustomUser
from .serializers import FollowSerializer

# Follow a user
class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        user_to_follow = self.get_object()
        request.user.following_users.add(user_to_follow)
        return Response({"detail": f"You are now following {user_to_follow.username}"}, status=status.HTTP_200_OK)


# Unfollow a user
class UnfollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        user_to_unfollow = self.get_object()
        request.user.following_users.remove(user_to_unfollow)
        return Response({"detail": f"You have unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)
