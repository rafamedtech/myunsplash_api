from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser

from .serializers import UploadSerializer
from .models import Upload

# Create your views here.

class UploadImage(APIView):

    parser_classes = [MultiPartParser, JSONParser, FormParser]

    def post(self, request, *args, **kwargs):

        serializer = UploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

class DeleteImage(APIView):

    def delete(self, request, pk, *args, **kwargs):
        image = Upload.objects.get(pk=pk)
        image.delete()

        return Response({'message': 'Image deleted'},status=204)