from django.urls import path
from . import views
from .views import getContactsAjax

app_name = 'sales'
urlpatterns = [
    path('create_sale/', views.createSale, name= 'sale_new'),
    path('sale_update/<int:pk>', views.saleUpdate, name= 'sale_update'),
    path('sale_list/', views.salesList, name='sale_list'),
    path('get-contacts-ajax/', views.getContactsAjax, name='get_contacts_ajax'),
    path('get-sale-ajax/', views.getSaleAjax, name='get_sale_ajax'),
]