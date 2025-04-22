from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogSerializer
from rest_framework.decorators import api_view
from blog.models import Blog

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