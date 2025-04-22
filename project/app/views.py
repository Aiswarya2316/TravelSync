from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.timezone import now




# Customer Registration
def customer_register(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer registered successfully!")
            return redirect("login")
    else:
        form = CustomerRegistrationForm()
    return render(request, "customer/register.html", {"form": form, "user_type": "Customer"})



# Seller Registration
def seller_register(request):
    if request.method == "POST":
        form = StafRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Seller registered successfully!")
            return redirect("login")
    else:
        form = StafRegistrationForm()
    return render(request, "staf/register.html", {"form": form, "user_type": "Staf"})



# Admin Registration
def admin_register(request):
    if request.method == "POST":
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Admin registered successfully!")
            return redirect("login")
    else:
        form = AdminRegistrationForm()
    return render(request, "admin/register.html", {"form": form, "user_type": "Admin"})



# --- User Login ---
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = None
            redirect_url = "login"  # Default in case of failure

            if Customer.objects.filter(email=email, password=password).exists():
                user = Customer.objects.get(email=email)
                request.session["user_type"] = "Customer"
                redirect_url = "customerhome"
            elif Staf.objects.filter(email=email, password=password).exists():
                user = Staf.objects.get(email=email)
                request.session["user_type"] = "Staf"
                redirect_url = "stafhome"
            elif AdminReg.objects.filter(email=email, password=password).exists():
                user = AdminReg.objects.get(email=email)
                request.session["user_type"] = "Admin"
                redirect_url = "adminhome"

            if user:
                request.session["user_id"] = user.id
                messages.success(request, f"Welcome {user.name}!")
                return redirect(redirect_url)
            else:
                messages.error(request, "Invalid credentials")

    form = LoginForm()
    return render(request, "login.html", {"form": form})



# Logout View
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("home")





def home(request):
    return render(request,'home.html')


def stafhome(request):
    return render(request,'staf/stafhome.html')


def customerhome(request):
    return render(request,'customer/customerhome.html')

from django.shortcuts import render
from .models import Customer, Staf, Booking, TourPackage, Hotel, Transport

def adminhome(request):
    total_users = Customer.objects.count()
    total_staff = Staf.objects.count()
    total_bookings = Booking.objects.count()
    total_packages = TourPackage.objects.count()
    total_hotels = Hotel.objects.count()
    total_transports = Transport.objects.count()

    context = {
        'total_users': total_users,
        'total_staff': total_staff,
        'total_bookings': total_bookings,
        'total_packages': total_packages,
        'total_hotels': total_hotels,
        'total_transports': total_transports,
    }
    return render(request, 'admin/adminhome.html', context)




from django.shortcuts import render, redirect
from .forms import TourPackageForm, TransportForm, HotelForm

# Add Tour Package
def add_tour_package(request):
    if request.method == "POST":
        form = TourPackageForm(request.POST, request.FILES)  # include request.FILES
        if form.is_valid():
            form.save()
            return redirect('add_tour')
    else:
        form = TourPackageForm()
    return render(request, 'staf/add_tour_package.html', {'form': form})

# Add Transport Details
def add_transport(request):
    if request.method == "POST":
        form = TransportForm(request.POST, request.FILES)  # include request.FILES
        if form.is_valid():
            form.save()
            return redirect('add_transport')
    else:
        form = TransportForm()
    return render(request, 'staf/add_transport.html', {'form': form})

# Add Hotel Details
def add_hotel(request):
    if request.method == "POST":
        form = HotelForm(request.POST, request.FILES)  # include request.FILES
        if form.is_valid():
            form.save()
            return redirect('add_hotel')
    else:
        form = HotelForm()
    return render(request, 'staf/add_hotel.html', {'form': form})


def view_tour_package(req):
    data=TourPackage.objects.all()
    return render(req,'staf/view_tour_package.html',{'data':data})

def view_transport(req):
    data=Transport.objects.all()
    return render(req,'staf/view_transport.html',{'data':data})

def view_hotel(req):
    data=Hotel.objects.all()
    return render(req,'staf/view_hotel.html',{'data':data})




def viewtourpackage(req):
    data=TourPackage.objects.all()
    return render(req,'customer/viewtourpackage.html',{'data':data})

def viewtransport(req):
    data=Transport.objects.all()
    return render(req,'customer/viewtransport.html',{'data':data})

def viewhotel(req):
    data=Hotel.objects.all()
    return render(req,'customer/viewhotel.html',{'data':data})




from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TourPackage, Hotel, Transport, Booking, Customer
from .forms import BookingForm

def get_logged_in_customer(request):
    """Utility function to fetch the logged-in customer"""
    user_id = request.session.get("user_id")
    if user_id:
        try:
            return Customer.objects.get(id=user_id)
        except Customer.DoesNotExist:
            return None
    return None

def book_package(request, package_id):
    customer = get_logged_in_customer(request)
    if not customer:
        messages.error(request, "You must be logged in to book a package.")
        return redirect("login")

    tour_package = TourPackage.objects.get(id=package_id)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = customer  # Assigning logged-in customer
            booking.tour_package = tour_package
            booking.save()
            messages.success(request, "Package booked successfully!")
            return redirect("view_bookings")
    else:
        form = BookingForm()
    return render(request, "customer/book_package.html", {"form": form, "tour_package": tour_package})


def book_hotel(request, hotel_id):
    customer = get_logged_in_customer(request)
    if not customer:
        messages.error(request, "You must be logged in to book a hotel.")
        return redirect("login")

    hotel = Hotel.objects.get(id=hotel_id)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = customer
            booking.hotel = hotel  # Ensure only hotel is assigned
            booking.tour_package = None  # Prevent package assignment
            booking.transport = None
            booking.save()
            messages.success(request, "Hotel booked successfully!")
            return redirect("view_bookings")
    else:
        form = BookingForm()
    return render(request, "customer/book_hotel.html", {"form": form, "hotel": hotel})


def book_transport(request, transport_id):
    customer = get_logged_in_customer(request)
    if not customer:
        messages.error(request, "You must be logged in to book transport.")
        return redirect("login")

    transport = Transport.objects.get(id=transport_id)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = customer
            booking.transport = transport  # Ensure only transport is assigned
            booking.tour_package = None
            booking.hotel = None
            booking.save()
            messages.success(request, "Transport booked successfully!")
            return redirect("view_bookings")
    else:
        form = BookingForm()
    return render(request, "customer/book_transport.html", {"form": form, "transport": transport})


def view_bookings(request):
    customer = get_logged_in_customer(request)
    if not customer:
        messages.error(request, "You must be logged in to view bookings.")
        return redirect("login")

    bookings = Booking.objects.filter(customer=customer)
    return render(request, "customer/view_bookings.html", {"bookings": bookings})





from django.shortcuts import render
from .models import TourPackage, Customer, Staf, Transport, Hotel

def admin_view_packages(request):
    packages = TourPackage.objects.all()
    return render(request, 'admin/view_packages.html', {'packages': packages})

def admin_view_users(request):
    users = Customer.objects.all()
    return render(request, 'admin/view_users.html', {'users': users})

def admin_view_staffs(request):
    staffs = Staf.objects.all()
    return render(request, 'admin/view_staffs.html', {'staffs': staffs})

def admin_view_transports(request):
    transports = Transport.objects.all()
    return render(request, 'admin/view_transports.html', {'transports': transports})

def admin_view_hotels(request):
    hotels = Hotel.objects.all()
    return render(request, 'admin/view_hotels.html', {'hotels': hotels})



from django.shortcuts import get_object_or_404

def delete_tour_package(request, pk):
    package = get_object_or_404(TourPackage, pk=pk)
    if request.method == "POST":
        package.delete()
        return redirect('view_tour')  

def delete_hotel(request, id):
    hotel = get_object_or_404(Hotel, id=id)
    hotel.delete()
    return redirect('view_hotel') 

def delete_transport(request, id):
    transport = get_object_or_404(Transport, id=id)
    if request.method == 'POST':
        transport.delete()
        return redirect('view_transport')