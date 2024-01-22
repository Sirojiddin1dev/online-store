from django.shortcuts import render
from main.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import *


"""  Start Filter API  """
@api_view(['GET'])
def filter_product_by_price(request):
    start_price = request.GET.get('s_price')
    end_price = request.GET.get('e_price')
    products = Product.objects.filter(price__gte=start_price, price__lte=end_price)
    ser = ProductSerializer(products, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_sub_category_by_category(request, pk):
    category = Category.objects.get(pk=pk)
    sub_category = Sub_category.objects.filter(category=category)
    sar = Sub_categorySerializer(sub_category, many=True)
    return Response(sar.data)


@api_view(['GET'])
def filter_product_by_sub_category(request, pk):
    sub_category = Sub_category.objects.get(pk=pk)
    product = Product.objects.filter(sub_category=sub_category)
    sar = ProductSerializer(product, many=True)
    return Response(sar.data)


@api_view(['GET'])
def filter_product_by_name(request):
    name = request.GET.get('name')
    product = Product.objects.filter(name__icontains=name)
    sar = ProductSerializer(product, many=True)
    return Response(sar.data)


@api_view(['GET'])
def filter_product_by_brand(request, pk):
    brand = Brand.objects.get(pk=pk)
    product = Product.objects.filter(brand=brand)
    sar = ProductSerializer(product, many=True)
    return Response(sar.data)


@api_view(['GET'])
def filter_product_by_is_sale(request):
    product = Product.objects.filter(is_sale=True)
    sar = ProductSerializer(product, many=True)
    return Response(sar.data)


@api_view(['GET'])
def filter_product_by_rating(request):
    product = Product.objects.filter().order_by('-rating')
    sar = ProductSerializer(product, many=True)
    return Response(sar.data)


@api_view(['GET'])
def filter_brand_by_name(request):
    name = request.GET.get('name')
    brand = Brand.objects.filter(name__icontains=name)
    sar = BrandSerializer(brand, many=True)
    return Response(sar.data)


@api_view(['GET'])
def filter_card_by_user(request, pk):
    user = User.objects.get(pk=pk)
    card = Card.objects.filter(user=user)
    sar = CardSerializer(card, many=True)
    return Response(sar.data)


@api_view(['GET'])
def filter_saved_by_user(request, pk):
    user = User.objects.get(pk=pk)
    saved = Saved.objects.filter(user=user)
    sar = SavedSerializer(saved, many=True)
    return Response(sar.data)


@api_view(['GET'])
def filter_order_by_user(request, pk):
    user = User.objects.get(pk=pk)
    order = Order.objects.filter(user=user)
    sar = OrderSerializer(order, many=True)
    return Response(sar.data)


@api_view(['GET'])
def filter_product_by_user(request, pk):
    user = User.objects.get(pk=pk)
    product = Product.objects.filter(user=user)
    sar = ProductSerializer(product, many=True)
    return Response(sar.data)


@api_view(['GET'])
def filter_office_by_address(request, pk):
    address = Region.objects.get(pk=pk)
    office = Office.objects.filter(region=address)
    sar = OfficeSerializer(office, many=True)
    return Response(sar.data)
"""    End filter API    """


"""   Start Get API   """
@api_view(['GET'])
def get_product_view(request):
    product = Product.objects.all()
    sar = ProductSerializer(product, many=True)
    return Response(sar.data)


@api_view(['GET'])
def get_brand_view(request):
    brand = Brand.objects.all()
    sar = BrandSerializer(brand, many=True)
    return Response(sar.data)


@api_view(['GET'])
def get_category_view(request):
    category = Category.objects.all()
    sar = CategorySerializer(category, many=True)
    return Response(sar.data)


@api_view(['GET'])
def get_sub_category_view(request):
    sub_category = Sub_category.objects.all()
    sar = Sub_categorySerializer(sub_category, many=True)
    return Response(sar.data)


@api_view(['GET'])
def get_color_view(request):
    color = Color.objects.all()
    sar = CategorySerializer(color, many=True)
    return Response(sar.data)
"""   End Get API   """
