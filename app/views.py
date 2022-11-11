from django.contrib.auth import get_user_model

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView

from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Post, PostImage
from .serializers import PostSerializer, PostImageSerializer, UserSerializer, SignInSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostImageViewSet(ModelViewSet):
    serializer_class = PostImageSerializer

    def get_serializer_context(self):
        return {'id': self.kwargs['pk']}

    def get_queryset(self):
        return Post.objects.filter(post_id=self.kwargs['pk'])

class SignUpView(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class SignInView(TokenObtainPairView):
    serializer_class = SignInSerializer