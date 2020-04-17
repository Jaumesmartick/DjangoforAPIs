from rest_framework import generics, permissions 
#permissions restrict the acces for the views depending on the user
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer

# Create your views here.
class PostList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated,) #Show the content for registered users
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticated,) #Show the content for registered users
    permission_classes = (IsAuthorOrReadOnly,) #Allows the author of the post modify the content, others can just read
    queryset = Post.objects.all()
    serializer_class = PostSerializer