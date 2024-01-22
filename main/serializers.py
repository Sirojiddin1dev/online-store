from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = models.Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"


class Sub_categorySerializer(serializers.ModelSerializer):
    class Meta:
        depth = 3
        model = models.Sub_category
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = "__all__"


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Color
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 3
        model = models.Card
        fields = "__all__"


class SavedSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 3
        model = models.Saved
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 3
        model = models.Order
        fields = "__all__"


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = models.Office
        fields = "__all__"
