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
    path('adminhome/',views.adminhome,name="adminhome"),
    path('add-tour/', views.add_tour_package, name='add_tour'),
    path('add-transport/', views.add_transport, name='add_transport'),
    path('add-hotel/', views.add_hotel, name='add_hotel'),
    path('view-tour/', views.view_tour_package, name='view_tour'),
    path('view-transport/', views.view_transport, name='view_transport'),
    path('view-hotel/', views.view_hotel, name='view_hotel'),
    path('view-tour-packages/', views.viewtourpackage, name='view_tour_packages'),
    path('view-transports/', views.viewtransport, name='view_transports'),
    path('view-hotels/', views.viewhotel, name='view_hotels'),
    path('delete-tour/<int:pk>/', views.delete_tour_package, name='delete_tour'),
    path('delete-hotel/<int:id>/', views.delete_hotel, name='delete_hotel'),
    path('delete-transport/<int:id>/', views.delete_transport, name='delete-transport'),

    path('book-package/<int:package_id>/', views.book_package, name='book_package'),
    path('book-hotel/<int:hotel_id>/', views.book_hotel, name='book_hotel'),
    path('book-transport/<int:transport_id>/', views.book_transport, name='book_transport'),

    path('view-bookings/', views.view_bookings, name='view_bookings'),


    path('adminpackages/', views.admin_view_packages, name='admin_view_packages'),
    path('adminusers/', views.admin_view_users, name='admin_view_users'),
    path('adminstaffs/', views.admin_view_staffs, name='admin_view_staffs'),
    path('admintransports/', views.admin_view_transports, name='admin_view_transports'),
    path('adminhotels/', views.admin_view_hotels, name='admin_view_hotels'),

]