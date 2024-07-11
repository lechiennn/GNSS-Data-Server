from rest_framework import serializers
from process.models import Data


class DataSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField()
    
    class Meta:
        model = Data
        fields = '__all__'