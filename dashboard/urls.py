from django.urls import path
from .views import *

urlpatterns = [
    # -----------------  CRUD Order path -----------------
    path('create-order/', create_order),
    path('update-order/<int:pk>/', update_order),
    path('delete-order/<int:pk>/', delete_order),

    # -----------------  CRUD Product path ---------------
    path('create-product/', create_product),
    path('edit-product/<int:pk>/', update_product),
    path('delete-product/<int:pk>/', delete_product),

    #-----------------  CRUD Objects path ----------------
    path('create-region/', create_region),
    path('update-region/<int:pk>/', update_region),
    path('delete-region/<int:pk>/', delete_region),

    path('create-category/', create_category),
    path('update-category/<int:pk>/', update_category),
    path('delete-category/<int:pk>/', delete_category),

    path('create-sub-category/', create_sub_category),
    path('edit-sub-category/<int:pk>/', update_sub_category),
    path('delete-sub-category/<int:pk>/', delete_sub_category),

    path('create-brand/', create_brand),
    path('edit-brand/<int:pk>/', update_brand),
    path('delete-brand/<int:pk>/', delete_brand),

    path('create-color/', create_color),
    path('edit-color/<int:pk>/', update_color),
    path('delete-color/<int:pk>/', delete_color),

    path('create-image/', create_image),
    path('edit-image/<int:pk>/', update_image),
    path('delete-image/<int:pk>/', delete_image),

    path('create-size-category/', create_size_category),
    path('edit-size-category/<int:pk>/', edit_size_category),
    path('delete-size-category/<int:pk>/', delete_size_category),

    path('create-card/', create_card),
    path('edit-card/<int:pk>/', edit_card),
    path('delete-card/<int:pk>/', delete_card),

    path('create-saved/', create_saved),
    path('edit-saved/<int:pk>/', edit_saved),
    path('delete-saved/<int:pk>/', delete_saved),

    path('create-office/', create_office),
    path('edit-office/<int:pk>/', edit_office),
    path('delete-office/<int:pk>/', delete_office),
]
