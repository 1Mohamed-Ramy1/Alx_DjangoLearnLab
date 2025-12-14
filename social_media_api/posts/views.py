from rest_framework import viewsets, generics, permissions
from rest_framework.filters import SearchFilter
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Comment, Like, Notification
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly

# Feed view
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def feed(request):
    user = request.user
    following_users = user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


# Post ViewSet
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# Comment ViewSet
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# Like a post
class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            Notification.objects.create(
                sender=request.user,
                receiver=post.author,
                post=post,
                notification_type='like'
            )
            return Response({"detail": "Post liked"}, status=200)
        return Response({"detail": "Already liked"}, status=200)


# Unlike a post
class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            Notification.objects.filter(
                sender=request.user,
                receiver=post.author,
                post=post,
                notification_type='like'
            ).delete()
            return Response({"detail": "Post unliked"}, status=200)
        except Like.DoesNotExist:
            return Response({"detail": "You haven't liked this post"}, status=400)
