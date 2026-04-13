from django.urls import path
# from .views import test_api
from .views import PostListCreateAPIView, PostDetailAPIView

urlpatterns = [
    # path('test/', test_api),
    path('posts/', PostListCreateAPIView.as_view()),
    path('posts/<int:pk>/', PostDetailAPIView.as_view()),
]