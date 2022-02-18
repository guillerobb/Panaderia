from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('list/', views.ProductListView.as_view(), name='product_list'),
    path('new/', views.ProductCreateView.as_view(),name='product_form'),
    path('<int:pk>/', views.ProductDetailView.as_view(),name='product_detail'),
    path('u/<int:pk>/', views.ProductUpdateView.as_view(),name='product_update'),
    path('d/<int:pk>/', views.ProductDeleteView.as_view(),name='product_delete'),
    path('prices/', views.priceUpdate, name='prices_update'),
]