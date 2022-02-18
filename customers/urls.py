from django.urls import path
from . import views

app_name = 'customers'
urlpatterns = [
    path('', views.index, name='index'),
    path('customers/', views.CustomerListView.as_view(), name='customer_list'),
    path('customers/new/', views.CustomerCreateView.as_view(), name='customer_form'),
    path('customers/<int:pk>/', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('customers/u/<int:pk>/', views.CustomerUpdateView.as_view(), name='customer_update'),
    path('customers/d/<int:pk>/', views.CustomerDeleteView.as_view(), name='customer_delete'),

    path('customers-contact/<int:customer_id>/', views.CustomerContactList, name='contact_list'),
    path('customers-contact-new/<int:customer_id>/', views.ContactCreateView, name='contact_add_form'),
    path('customers-contact-add/<int:customer_id>/', views.AddContact, name='contact_add'),
    path('customers-contact-update/<int:contact_id>/', views.ContactUpdateView, name='contact_update'),
    path('customers-contact-delete/<int:pk>/', views.ContactDeleteView.as_view(), name='contact_delete'),
]