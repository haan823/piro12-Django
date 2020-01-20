from django.urls import path
from shop import views

app_name = 'shop'
urlpatterns = [
    path('shop/', views.item_list),
]