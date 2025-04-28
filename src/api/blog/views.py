from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogSerializer
from rest_framework.decorators import api_view
from blog.models import Blog
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

@api_view(['GET','POST'])
def get_list_blog(request):
    if request.method == "GET":
        blogs = Blog.objects.all()
        result = BlogSerializer(blogs, many=True)
        print(result.data)
        return Response({"data": result.data})
    elif request.method == "POST":
        serializer = BlogSerializer(data=request.data)
        print(serializer, serializer.is_valid())
        if serializer.is_valid():
            result = serializer.save()
            print(result)
            return Response({"data": "success"}, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def detail_blog(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response({"error": "Could not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = BlogSerializer(blog, data=request.data)
        print(serializer.is_valid(), serializer)
        if serializer.is_valid():
            serializer.save()
            print(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Could not edit"}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FBVAPIBlog(APIView):
    def get(self, request):
        blog = Blog.objects.all()
        result = BlogSerializer(blog, many=True)
        return Response({"data": result.data})

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FBVAPIBlogDetail(APIView):
    def get(self, request, pk):
        try:
            blog = Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return Response({"Error": "Could not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    def put(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"Error": "Could not edit"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        blog.delete()
        return Response("Blog successfully deleted", status=status.HTTP_204_NO_CONTENT)

class BlogGenericAPIView(GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get(self, request):
        books = self.get_queryset()
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class BlogGenericDetailAPIView(GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    def get(self, request, *args, **kwargs):
        blog = self.get_object()
        serializer = self.get_serializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        blog = self.get_object()
        serializer = self.get_serializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"Error":"request not valid"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        blog = self.get_object()
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BlogGenericAPIViewMixin(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class BlogGenericDetailAPIViewMixin(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ConcreateAPIView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class ConcreateDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer