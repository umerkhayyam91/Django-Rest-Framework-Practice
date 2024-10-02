from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ItemSerializer
from base.models import Items

@api_view(['GET'])
def getItems(request):
    items = Items.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItems(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)