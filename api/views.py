from django.shortcuts import render
from rest_framework import generics
from mainapp.models import Blog
from .serializers import BlogSerializer





class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer    
# Create your views here.

