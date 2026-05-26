from django.urls import path
from .views import home, signup, login_view, logout_view, profile, add_to_cart, cart, remove_from_cart
from .views import add_product
from .views import delete_product
from .views import product_detail
from .views import edit_product

urlpatterns = [

    path('', home, name='home'),

    path('signup/', signup, name='signup'),

    path('login/', login_view, name='login'),

    path('logout/', logout_view, name='logout'),

    path('profile/', profile, name='profile'),

    path(
    'add-to-cart/<int:product_id>/',
    add_to_cart,
    name='add_to_cart'),

    path('cart/', cart, name='cart'),
    path(
    'remove-from-cart/<int:cart_id>/',
    remove_from_cart,
    name='remove_from_cart'),
    path('add-product/', add_product, name='add_product'),
    path(
    'delete-product/<int:product_id>/',
    delete_product,
    name='delete_product'),
    path(
    'edit-product/<int:product_id>/',
    edit_product,
    name='edit_product'
),
    path(
    'product/<int:product_id>/',
    product_detail,
    name='product_detail'),
    
]