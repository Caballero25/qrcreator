from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
import cv2
from PIL import Image
import numpy as np

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


class DecodeQrView(APIView):
    serializer_class = QRCodeSerializer
    def post(self, request, *args, **kwargs):
        # Obtener la imagen del request
        image = request.data.get('image')
        pil_image = Image.open(image)
        image_np = np.array(pil_image)
        detector = cv2.QRCodeDetector()
        data = detector.detectAndDecode(image_np)
        return Response({'data': data[0]}, status=status.HTTP_201_CREATED)