from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from .models import Recycleable, Phone

def hero_view(request):
    return render(request, 'main/hero.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            user.save()
            login(request, user)
            if request.user.is_staff:
                return redirect('recycler_home')
            return redirect('home')
        else:
            return render(request, 'main/login.html', {'error': 'Invalid email id or password'})
    else:
        return render(request, 'main/login.html')

def signup_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        phone_no = request.POST['phone']
        try:
            user = User.objects.create_user(username=email, password=password, email=email)
            user.save()
            phone = Phone.objects.create(user=user, phone_no=phone_no)
            phone.save()
            login(request, user)
            return redirect('home')
        except:
            return render(request, 'index.html', {'error': 'An error occurred'})
    else:
        return render(request, 'main/signup.html')

def logout_view(request):
    logout(request)
    return redirect('login') # Redirect to login page after logout

@login_required
def home_view(request):
    return render(request, 'main/dashboard.html')

@login_required
def list_view(request):
    items = Recycleable.objects.filter(user=request.user)
    return render(request, 'main/mylist.html')

@login_required
def create_item(request):
    return render(request, 'main/form.html')

#@login_required
#def save_item(request):

@staff_member_required
def recycler_home(request):
    return render(request, 'main/recycler_dash.html')

