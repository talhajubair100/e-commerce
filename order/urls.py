from django.urls import path 
from .views import order, add_to_shopcart, shopcart

urlpatterns = [
   path('', order, name='order'),
   path('shopcart', shopcart, name='shopcart'),
   path('add_to_shopcart/<int:id>', add_to_shopcart, name='add_to_shopcart')

]
