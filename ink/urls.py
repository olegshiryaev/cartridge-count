from ink import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.show_all_device, name="home"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cartridges/', views.cartridgeList, name="cartridges"),
    path('device/<pk>/', views.show_one_device, name="device"),
    path('device_create', views.device_create, name="device_create"),
    path('device_update', views.device_update, name="device_update"),
    # path('mount_form/', views.createMount, name="createMount"),
    path('create_mount/<int:pk>/', views.createMount, name="create_mount"),
    path('update_mount/<int:pk>/', views.updateMount, name="update_mount"),
    path('delete_mount/<int:pk>/', views.deleteMount, name="delete_mount"),
]
