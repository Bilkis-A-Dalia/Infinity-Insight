from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views
router = DefaultRouter() #this is router

router.register('category', views.CategoryViewSet) #one-->antena
router.register('article', views.ArticleViewSet) #one-->antena
router.register('reviews', views.ReviewViewSet) #one-->antena
urlpatterns = [
    path('', include(router.urls)),

]