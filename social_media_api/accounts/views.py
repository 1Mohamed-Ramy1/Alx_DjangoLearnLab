from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from rest_framework.decorators import action
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import FollowSerializer
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key
        })

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key
        })

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def follow(self, request, pk=None):
        user_to_follow = self.get_object()
        request.user.following_users.add(user_to_follow)
        return Response({"detail": f"You are now following {user_to_follow.username}"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def unfollow(self, request, pk=None):
        user_to_unfollow = self.get_object()
        request.user.following_users.remove(user_to_unfollow)
        return Response({"detail": f"You have unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)
