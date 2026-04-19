from django.urls import path, include
# from .views import test_api
# from .views import PostListCreateAPIView, PostDetailAPIView
from rest_framework.routers import DefaultRouter
from .views import PostViewSet
from .views import RegisterAPIView, LoginAPIView, LogoutAPIView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('posts', PostViewSet)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    # path('test/', test_api),
    # path('posts/', PostListCreateAPIView.as_view()),
    # path('posts/<int:pk>/', PostDetailAPIView.as_view()),

    path('', include(router.urls)),
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
