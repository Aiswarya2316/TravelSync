from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path("registerparent/", views.customer_register, name="customer_register"),
    path("registerstaf/", views.seller_register, name="seller_register"),
    path("registeradmin/", views.admin_register, name="admin_register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path('stafhome/',views.stafhome,name='stafhome'),
    path('customerhome/',views.customerhome,name='customerhome'),
    path('add-tour/', views.add_tour_package, name='add_tour'),
    path('add-transport/', views.add_transport, name='add_transport'),
    path('add-hotel/', views.add_hotel, name='add_hotel'),
    path('view-tour/', views.view_tour_package, name='view_tour'),
    path('view-transport/', views.view_transport, name='view_transport'),
    path('view-hotel/', views.view_hotel, name='view_hotel'),

]