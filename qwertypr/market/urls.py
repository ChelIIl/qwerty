from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name='home'),
    path('product/<int:product_id>', product_info, name='product'),
    path('user/sign_in/', sign_in, name='sign_in'),
    path('user/register/', register, name='register'),
]
