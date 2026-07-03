from rest_framework import serializers
from .models import  Product

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    barcode =serializers.CharField(max_length=20)
    stock_quantity = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        fields=('name', 'barcode', 'price')

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
