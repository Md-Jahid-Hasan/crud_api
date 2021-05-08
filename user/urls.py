from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.UserLoginView.as_view()),
    path('feed/', views.ProfileFeedViewSet.as_view()),
]