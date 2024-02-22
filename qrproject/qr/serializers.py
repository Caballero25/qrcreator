# serializers.py
from rest_framework import serializers
from .models import QrModel

class QRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QrModel
        fields = '__all__'
