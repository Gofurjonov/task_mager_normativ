# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post
from .serializers import PostSerializer
from django.contrib.auth import authenticate, login, logout


# 1-normativ

# @api_view(['GET'])
# def test_api(request):
#     return Response({
#         "message": "Hello DRF"
#     })


# 2-normativ
# class PostListCreateAPIView(APIView):
#
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class PostDetailAPIView(APIView):
#
#     def get_object(self, pk):
#         try:
#             return Post.objects.get(id=pk)
#         except Post.DoesNotExist:
#             return None
#
#     def get(self, request, pk):
#         post = self.get_object(pk)
#         if not post:
#             return Response({"error": "Post topilmadi"}, status=404)
#
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         post = self.get_object(pk)
#         if not post:
#             return Response({"error": "Post topilmadi"}, status=404)
#
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#
#     def delete(self, request, pk):
#         post = self.get_object(pk)
#         if not post:
#             return Response({"error": "Post topilmadi"}, status=404)
#
#         post.delete()
#         return Response({"message": "Post o‘chirildi"}, status=204)


# 3-normativ
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class RegisterAPIView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')

        if password != confirm_password:
            return Response({"error": "Parollar mos emas"}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({"error": "User mavjud"}, status=400)

        user = User(username=username)
        user.set_password(password)
        user.save()

        return Response({"message": "User yaratildi"}, status=201)

class LoginAPIView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is None:
            return Response({"error": "Login yoki parol noto‘g‘ri"}, status=400)

        login(request, user)
        return Response({"message": "Muvaffaqiyatli login"})


class LogoutAPIView(APIView):

    def post(self, request):
        logout(request)
        return Response({"message": "Logout qilindi"})