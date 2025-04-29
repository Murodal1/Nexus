from rest_framework.response import Response
from rest_framework import status
from .serializers import CategorySerializer
from rest_framework.decorators import api_view
from category.models import Category
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet

@api_view(['GET','POST'])
def get_list_ctg(request):
    if request.method == "GET":
        categories = Category.objects.all()
        result = CategorySerializer(categories, many=True)
        print(result.data)
        return Response({"data": result.data})
    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        print(serializer, serializer.is_valid())
        if serializer.is_valid():
            result = serializer.save()
            print(result)
            return Response({"data": "success"}, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def detail_ctg(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({"error": "Could not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = CategorySerializer(category, data=request.data)
        print(serializer.is_valid(), serializer)
        if serializer.is_valid():
            serializer.save()
            print(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Could not edit"}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        result = CategorySerializer(categories, many=True)
        return Response({"data": result.data})

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            result = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):
    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"Error": "Could not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"Error": "Could not edit"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response("Category successful deleted",status=status.HTTP_204_NO_CONTENT)

class CategoryGenericAPIView(GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request):
        books = self.get_queryset()
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class CategoryGenericDetailAPIView(GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def get(self, request, *args, **kwargs):
        category = self.get_object()
        serializer = self.get_serializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        category = self.get_object()
        serializer = self.get_serializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"Error":"request not valid"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        category = self.get_object()
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryGenericAPIViewMixin(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CategoryGenericDetailAPIViewMixin(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ConcreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ConcreateDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer