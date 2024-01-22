from django.shortcuts import render
from main.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import *


"""  Start Order CRUD  """
@api_view(['POST'])
def create_order(request):
    user = request.POST['user']
    card = request.POST.getlist('card')
    pass_number = request.POST['pass_number']
    is_delivery = request.POST['is_delivery']
    extra_phone_number = request.POST['extra_phone_number']
    payment_type = request.POST['payment_type']
    office = request.POST['office']
    lat = request.POST['lat']
    lot = request.POST['lot']
    order = Order.objects.create(
        user_id = user,
        pass_number = pass_number,
        is_delivery = is_delivery,
        extra_phone_number = extra_phone_number,
        payment_type = payment_type,
        office_id = office,
        lat = lat,
        lot = lot,
    )
    for i in card:
        order.card.add(i)
        order.save()
    sar = OrderSerializer(order)
    return Response(sar.data)


@api_view(['PUT'])
def update_order(request, pk):
    user = request.POST.get('user')
    card = request.POST.getlist('card')
    pass_number = request.POST.get('pass_number')
    is_delivery = request.POST.get('is_delivery')
    extra_phone_number = request.POST.get('extra_phone_number')
    payment_type = request.POST.get('payment_type')
    office = request.POST.get('office')
    lat = request.POST.get('lat')
    lot = request.POST.get('lot')
    order = Order.objects.get(pk=pk)
    order.user_id = user
    order.pass_number = pass_number
    order.is_delivery = is_delivery
    order.office_id = office
    order.lat = lat
    order.lot = lot
    if extra_phone_number is not None:
        order.extra_phone_number = extra_phone_number
    if card is not None:
        for i in card:
            order.card.add(i)
    order.save()
    sar = OrderSerializer(order)
    return Response(sar.data)


@api_view(['DELETE'])
def delete_order(request, pk):
    order = Order.objects.get(pk=pk)
    order.delete()
    return Response({'message':'Order deleted'})

"""  End Order CRUD  """


"""    Start Product CRUD     """

@api_view(['POST'])
def create_product(request):
    user = request.POST.get('user')
    name = request.POST.get('name')
    sub_category = request.POST.get('sub_category')
    brand = request.POST.get('brand')
    color = request.POST.getlist('color')
    photos = request.POST.getlist('photos')
    quantity = request.POST.get('quantity')
    features = request.POST.get('features')
    description = request.POST.get('description')
    price = request.POST.get('price')
    is_sale = request.POST.get('is_sale')
    old_cost = request.POST.get('old_cost')
    discount_percent = request.POST.get('discount_percent')
    is_banner = request.POST.get('is_banner')
    is_delivery = request.POST.get('is_delivery')
    rating = request.POST.get('rating')
    is_active = request.POST.get('is_active')
    size_category = request.POST.get('size_category')
    product = Product.objects.create(
        user_id=user,
        name=name,
        sub_category_id=sub_category,
        brand_id=brand,
        quantity=quantity,
        features=features,
        description=description,
        price=price,
        is_sale=is_sale,
        old_cost=old_cost,
        discount_percent=discount_percent,
        is_banner=is_banner,
        is_delivery=is_delivery,
        rating=rating,
        is_active=is_active,
        size_category_id=size_category,
    )
    for i in color:
        colors = Color.objects.get(pk=i)
        product.color.add(i)
    for image in photos:
        x = Image.objects.create(img=image)
        product.photos.add(x)
    product.save()
    sar = ProductSerializer(product)
    return Response(sar.data)


@api_view(['PUT'])
def update_product(request,pk):
    user = request.POST.data.get('user')
    name = request.POST.data.get('name')
    sub_category = request.POST.data.get('sub_category')
    brand = request.POST.data.get('brand')
    color = request.POST.getlist('color')
    photos = request.POST.getlist('photos')
    quantity = request.POST.data.get('quantity')
    features = request.POST.data.get('features')
    description = request.POST.data.get('description')
    price = request.POST.data.get('price')
    is_sale = request.POST.data.get('is_sale')
    old_cost = request.POST.data.get('old_cost')
    discount_percent = request.POST.data.get('discount_percent')
    is_banner = request.POST.data.get('is_banner')
    is_delivery = request.POST.data.get('is_delivery')
    rating = request.POS.POST.data.get('is_active')
    size_category = request.POST.data.get('size_category')
    is_active = request.POST.data.get('is_active')
    product = Product.objects.get(pk=pk)
    product.user_id = user
    product.name = name
    product.sub_category_id = sub_category
    product.brand_id = brand
    product.quantity = quantity
    product.features = features
    product.description = description
    product.price = price
    product.is_sale = is_sale
    product.old_cost = old_cost
    product.discount_percent = discount_percent
    product.is_banner = is_banner
    product.is_delivery = is_delivery
    product.rating = rating
    product.size_category_id = size_category
    product.is_active = is_active
    for i in color:
        colors = Color.objects.filter(id__in=i)
        product.color.set(colors)
    for i in photos:
        photo = Image.objects.filter(id__in=i)
        product.photos.set(photo)
    product.save()
    sar = ProductSerializer(product)
    return Response(sar.data)


@api_view(['DELETE'])
def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return Response({'message':'deleted'})

"""   Start objects CRUD   """
@api_view(['POST'])
def create_region(request):
    name = request.POST['name']
    region = Region.objects.create(
        name=name
    )
    sar = RegionSerializer(region)
    return Response(sar.data)


@api_view(['PUT'])
def update_region(request, pk):
    name = request.POST['name']
    region = Region.objects.get(pk=pk)
    region.name = name
    region.save()
    sar = RegionSerializer(region)
    return Response(sar.data)


@api_view(['DELETE'])
def delete_region(request, pk):
    region = Region.objects.get(pk=pk)
    region.delete()
    return Response({'message':'deleted'})


@api_view(['POST'])
def create_category(request):
    name = request.POST['name']
    category = Category.objects.create(
        name=name
    )
    sar = CategorySerializer(category)
    return Response(sar.data)


@api_view(['PUT'])
def update_category(request, pk):
    name = request.POST['name']
    category = Category.objects.get(pk=pk)
    category.name = name
    category.save()
    sar = CategorySerializer(category)
    return Response(sar.data)


@api_view(['DELETE'])
def delete_category(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return Response({'message':'deleted'})


@api_view(['POST'])
def create_sub_category(request):
    name = request.POST['name']
    category = request.POST['category']
    sub_category = Sub_category.objects.create(
        name=name,
        category=category
    )
    sar = Sub_categorySerializer(sub_category)
    return Response(sar.data)


@api_view(['PUT'])
def update_sub_category(request, pk):
    name = request.POST['name']
    category = request.POST['category']
    sub_category = Sub_category.objects.get(pk=pk)
    sub_category.name = name
    sub_category.category = category
    sub_category.save()
    sar = Sub_categorySerializer(sub_category)
    return Response(sar.data)


@api_view(['DELETE'])
def delete_sub_category(request, pk):
    sub_category = Sub_category.objects.get(pk=pk)
    sub_category.delete()
    return Response({'message':'deleted'})


@api_view(['POST'])
def create_brand(request):
    name = request.POST['name']
    brand = Brand.objects.create(
        name=name
    )
    sar = BrandSerializer(brand)
    return Response(sar.data)


@api_view(['PUT'])
def update_brand(request, pk):
    name = request.POST['name']
    brand = Brand.objects.get(pk=pk)
    brand.name = name
    brand.save()
    sar = BrandSerializer(brand)
    return Response(sar.data)


@api_view(['DELETE'])
def delete_brand(request, pk):
    brand = Brand.objects.get(pk=pk)
    brand.delete()
    return Response({'message':'deleted'})


@api_view(['POST'])
def create_color(request):
    name = request.POST['name']
    color = Color.objects.create(
        name=name
    )
    sar = ColorSerializer(color)
    return Response(sar.data)


@api_view(['PUT'])
def update_color(request, pk):
    name = request.POST['name']
    color = Color.objects.get(pk=pk)
    color.name = name
    color.save()
    sar = ColorSerializer(color)
    return Response(sar.data)


@api_view(['DELETE'])
def delete_color(request, pk):
    color = Color.objects.get(pk=pk)
    color.delete()
    return Response({'message':'deleted'})


@api_view(['POST'])
def create_image(request):
    img = request.FILES('img')
    image = Image.objects.create(
        img=img
    )
    sar = ImageSerializer(image)
    return Response(sar.data)


@api_view(['PUT'])
def update_image(request, pk):
    img = request.data.get('img')
    image = Image.objects.get(pk=pk)
    image.name = name
    image.save()
    sar = ColorSerializer(image)
    return Response(sar.data)


@api_view(['DELETE'])
def delete_image(request, pk):
    image = Image.objects.get(pk=pk)
    image.delete()
    return Response({'message':'deleted'})


""" Start Size_category CRUD """


@api_view(['POST'])
def create_size_category(request):
    name = request.POST['name']
    size_category = Size_category.objects.create(name=name)
    ser = Size_categorySerializer(size_category)
    return Response(ser.data)


@api_view(['PUT'])
def edit_size_category(request, pk):
    size_category = Size_category.objects.get(pk=pk)
    name = request.data.get('name')
    if name is not None:
        size_category.name = name
    size_category.save()
    ser = BrandSerializer(size_category)
    return Response(ser.data)


@api_view(['DELETE'])
def delete_size_category(request, pk):
    size_category = Size_category.objects.get(pk=pk)
    size_category.delete()
    return Response({'message': "Size_category obyekti o'chirildi"})


""" End Size_category CRUD """

""" Start Card CRUD """


@api_view(['POST'])
def create_card(request):
    user = request.POST['user']
    product = request.POST['product']
    total_price = request.POST['total_price']
    quantity = request.POST['quantity']
    card = Card.objects.create(
        user_id=user,
        product_id=product,
        total_price=total_price,
        quantity=quantity,
    )
    ser = CardSerializer(card)
    return Response(ser.data)


@api_view(['PUT'])
def edit_card(request, pk):
    card = Card.objects.get(pk=pk)
    user = request.data.get('user')
    product = request.data.get('product')
    total_price = request.data.get('total_price')
    quantity = request.data.get('quantity')
    if user is not None:
        card.user_id = user
    if product is not None:
        card.product_id = product
    if total_price is not None:
        card.total_price = total_price
    if quantity is not None:
        card.quantity = quantity
    card.save()
    ser = CardSerializer(card)
    return Response(ser.data)


@api_view(['DELETE'])
def delete_card(request, pk):
    card = Card.objects.get(pk=pk)
    card.delete()
    return Response({'message': "Card obyekti o'chirildi"})


""" End Card CRUD """

""" Start Saved CRUD """


@api_view(['POST'])
def create_saved(request):
    user = request.POST['user']
    product = request.POST.getlist('product')
    saved = Saved.objects.create(
        user_id=user,
    )
    for i in product:
        product = Product.objects.get(pk=i)
        saved.product.add(product)
    ser = SavedSerializer(saved)
    return Response(ser.data)


@api_view(['PUT'])
def edit_saved(request, pk):
    saved = Saved.objects.get(pk=pk)
    user = request.data.get('user')
    product = request.data.getlist('product')
    if user is not None:
        saved.user_id = user
    if product is not None:
        product = Product.objects.filter(id__in=product)
        saved.product.set(product)
    saved.save()
    ser = SavedSerializer(saved)
    return Response(ser.data)


@api_view(['DELETE'])
def delete_saved(request, pk):
    saved = Saved.objects.get(pk=pk)
    saved.delete()
    return Response({'message': "Saved obyekti o'chirildi"})


""" End Saved CRUD """

""" Start Office CRUD """


@api_view(['POST'])
def create_office(request):
    name = request.POST['name']
    number = request.POST['number']
    address = request.POST['address']
    office = Office.objects.create(
        name=name,
        number=number,
        address_id=address,
    )
    ser = OfficeSerializer(office)
    return Response(ser.data)


@api_view(['PUT'])
def edit_office(request, pk):
    office = Office.objects.get(pk=pk)
    name = request.data.get('name')
    number = request.data.get('number')
    address = request.data.get('address')
    if name is not None:
        office.name = name
    if number is not None:
        office.number = number
    if address is not None:
        office.address_id = address
    office.save()
    ser = OfficeSerializer(office)
    return Response(ser.data)


@api_view(['DELETE'])
def delete_office(request, pk):
    office = Office.objects.get(pk=pk)
    office.delete()
    return Response({'message': "Office obyekti o'chirildi"})


""" End Office CRUD """