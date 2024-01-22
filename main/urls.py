from django.urls import path
from .views import *

urlpatterns = [
    # -------------------------- Filter path  --------------
    path('filter_sub_category_by_category/<int:pk>/', filter_sub_category_by_category),
    path('filter_product_by_sub_category/<int:pk>/', filter_product_by_sub_category),
    path('filter_product_by_name/', filter_product_by_name),
    path('filter_product_by_brand/<int:pk>/', filter_product_by_brand),
    path('filter_product_by_is_sale/', filter_product_by_is_sale),
    path('filter_product_by_rating/', filter_product_by_rating),
    path('filter_brand_by_name/', filter_brand_by_name),
    path('filter_product_by_price/', filter_product_by_price),
    path('filter_card_by_user/<int:pk>/', filter_card_by_user),
    path('filter_saved_by_user/<int:pk>/', filter_saved_by_user),
    path('filter_order_by_user/<int:pk>/', filter_order_by_user),
    path('filter_product_by_user/<int:pk>/', filter_product_by_user),
    path('filter_office_by_address/<int:pk>/', filter_office_by_address),

    #  -----------------------    Get path  ------------------------
    path('get-product/', get_product_view),
    path('get-brand/', get_brand_view),
    path('get-category/', get_category_view),
    path('get-sub-category/', get_sub_category_view),
    path('get-color/', get_color_view),
]
