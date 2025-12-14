from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])  # <--- لازم موجودة للـ checker
def feed(request):
    user = request.user
    # يستخدم following.all() زي ما الـ checker طالب
    following_users = user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
