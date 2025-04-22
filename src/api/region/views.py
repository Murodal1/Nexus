from rest_framework.response import Response
from rest_framework import status
from .serializers import RegionSerializer
from rest_framework.decorators import api_view
from category.models import Region

@api_view(['GET','POST'])
def get_list_rgn(request):
    if request.method == "GET":
        regions = Region.objects.all()
        result = RegionSerializer(regions, many=True)
        print(result.data)
        return Response({"data": result.data})
    elif request.method == "POST":
        serializer = RegionSerializer(data=request.data)
        print(serializer, serializer.is_valid())
        if serializer.is_valid():
            result = serializer.save()
            print(result)
            return Response({"data": "success"}, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def detail_rgn(request, pk):
    try:
        region = Region.objects.get(pk=pk)
    except Region.DoesNotExist:
        return Response({"error": "Could not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = RegionSerializer(region)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = RegionSerializer(region, data=request.data)
        print(serializer.is_valid(), serializer)
        if serializer.is_valid():
            serializer.save()
            print(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Could not edit"}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        region.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)