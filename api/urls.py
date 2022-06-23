from django.urls import path
from . import views

urlpatterns = [
  path('', views.get_items),
  path('add/', views.add_item)
]