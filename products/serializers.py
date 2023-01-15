from rest_framework import serializers

from .models import Product, Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())
    brand_details = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_brand_details(self, obj):
        return BrandSerializer(obj.brand).data
