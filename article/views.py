from django.shortcuts import render
from rest_framework import viewsets,mixins
from .import models
from .import serializers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import views, status,filters,pagination
from rest_framework.response import Response
# Create your views here.

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

class ArticlePagination(pagination.PageNumberPagination):
    page_size=5
    page_size_query_param=page_size
    max_page_size=100

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class=ArticlePagination
    search_fields = ['headline', 'category__name']

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer