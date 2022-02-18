from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
	path('accounts/', views.UserListView.as_view(), name="users_list"),
    path('accounts/new/', views.UserCreateView.as_view(), name="user_create"),
	path('accounts/<int:pk>/', views.UserDetailView.as_view(), name="user_detail"),
	path('accounts/d/<int:pk>/', views.UserDeleteView.as_view(), name="user_delete"),
	path('accounts/u/<int:pk>/', views.UserUpdateView.as_view(), name="user_update"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
]