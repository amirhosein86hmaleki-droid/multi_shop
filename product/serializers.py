from rest_framework import serializers

from .models import Product, Color, Size

class PrDetailSerializer(serializers.ModelSerializer):
    color = serializers.StringRelatedField(many=True)
    size = serializers.StringRelatedField(many=True)
    class Meta:
        model = Product
        fields = '__all__'
        read_only = ('status','slug')
        extra_kwargs = {
            field.name: {'required': False}
            for field in Product._meta.fields
        }

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'