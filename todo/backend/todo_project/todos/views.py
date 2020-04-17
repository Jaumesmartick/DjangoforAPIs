from rest_framework import generics
from .models import Todo 
from .serializers import TodoSerializer

class ListTodo(generics.ListAPIView): #ListApiView to show the entire data
    queryset = Todo.objects.all() 
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveAPIView): #RetrieveAPIView to show a single element
    queryset = Todo.objects.all() 
    serializer_class = TodoSerializer
