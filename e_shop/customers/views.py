from django.shortcuts import render, redirect
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout as logout_user
from django.contrib import messages
from .models import Customer, User, Address, DISTRICT_LIST

# Create your views here.
def authentication(request):
    if request.POST:
        action = request.POST.get('action')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if action == 'signup':
            try:
                name = request.POST.get('name')
                phone = request.POST.get('phone')
                if not email or not password or not name or not phone:
                    raise ValueError('missing values')
                # create core user
                user_obj = User.objects.create_user(username=email, password=password)
                # create customer
                Customer.objects.create(core_user=user_obj, name=name, phone=phone)
            except IntegrityError as e:
                messages.error(request, 'Account already exists please Login !')
            except ValueError as e:
                messages.error(request, 'Fill out all fields !')
        elif action == 'login':
            if (user := authenticate(request, username=email, password=password)):
                login(request, user)
                return redirect('../')
            else:
                messages.error(request, 'Invalid credentials !')

    return render(request, 'customers/signup-login.html')

def logout(request):
    logout_user(request)
    return redirect('../../')

def add_address(request):
    districts = [dist[1] for dist in DISTRICT_LIST]
    user = request.user
    if not user.is_authenticated:
        messages.error(request, 'You are not logged in')
        return redirect('../../auth/')
    addresses = user.customer.address
    if request.POST:
        district = request.POST.get('district')
        city = request.POST.get('city')
        street = request.POST.get('street')
        building_no = request.POST.get('building')
        if district not in districts or not city or not building_no:
            messages.error(request, 'Fill out all required fields !')
        else:
            Address.objects.create(
                customer=user.customer,
                district=district,
                city=city,
                street=street,
                building_no=building_no
            )
    elif (pk := request.GET.get('del')):
        Address.objects.get(pk=pk).delete()
    districts.sort()
    return render(request, 'customers/add_address.html', {'districts': districts, 'addresses': addresses})