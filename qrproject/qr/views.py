from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

class CreateQrAPIView(APIView):
    serializer_class = QRCodeSerializer

    def post(self, request):
        text = request.data.get('text')
        serializer = QRCodeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status' : True,
                'message' : 'Success',
                'Data' : serializer.data},
                status=status.HTTP_201_CREATED)
        else :
            return Response({
                'status' : False,
                'message' : "Error"},
                status = status.HTTP_400_BAD_REQUEST)


class ImageUploadView(APIView):
    def post(self, request, *args, **kwargs):
        # Obtener la imagen del request
        imagen = request.data.get('imagen')

        # Aquí puedes realizar cualquier procesamiento que necesites con la imagen
        # Por ejemplo, puedes guardarla en tu sistema de archivos, base de datos, etc.

        # Devuelve la URL predefinida
        url_predefinida = "https://ejemplo.com/imagen_predefinida.jpg"
        return Response({'url': url_predefinida}, status=status.HTTP_201_CREATED)