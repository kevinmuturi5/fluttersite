from django.urls import path

from . import views

urlpatterns = [
  path('contact', views.contact, name='contact'),
  path('checkout<int:product_id>',views.checkout, name='checkout')

]