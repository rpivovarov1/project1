from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main),
    path('booking/', views.book_table),
    path('menu/', views.menu),
]
