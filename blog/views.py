from rest_framework import viewsets
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from dj_rest_auth.serializers import TokenSerializer

class post_view(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class LoginView(viewsets.ModelViewSet):
    serializer_class = TokenSerializer

