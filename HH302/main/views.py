from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from .models import Recycleable, Phone
from inference_sdk import InferenceHTTPClient
from django.http import HttpResponse
import uuid
import os

#Image Predictor
def image_predicter(path):
    CLIENT = InferenceHTTPClient(
        api_url="https://serverless.roboflow.com",
        api_key="x2P8cdyvpvNtakN5oHZC"   # paste your Roboflow API key
    )

    # Run inference on an image
    result = CLIENT.infer(
        path,   # replace with the path to your local image
        model_id="e-waste-dataset-r0ojc/43"  # model name and version
    )

    return(result['predictions'][0]['class'])


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
            return render(request, 'main/signup.html', {'error': 'An error occurred'})
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
    return render(request, 'main/mylist.html',{'data':items})

@login_required
def create_item(request):
    if request.method == 'POST':
        quantity = request.POST.get("quantity")
        image = request.FILES.get('image')

        if image:
            # Generate a unique filename
            ext = image.name.split('.')[-1]  # Extract the file extension
            filename = f"{uuid.uuid4().hex}.{ext}"  # Generate a unique filename

            # Save the image to the file system
            media_root = os.path.join('media', 'images')
            if not os.path.exists(media_root):
                os.makedirs(media_root)
            image_path = os.path.join(media_root, filename)
            
            with open(image_path, 'wb') as f:
                for chunk in image.chunks():
                    f.write(chunk)

            # Save the image metadata in the database
            form_save = Recycleable(user = request.user, image=f"images/{filename}", quantity = quantity)
            form_save.save()
            prediction = image_predicter(image_path)
            html_content = "<h2>The given image is of a "+prediction+"</h2>"
            return HttpResponse(html_content)
            # return redirect('list_view')
    else:
        return render(request, 'main/form.html')


@staff_member_required
def recycler_home(request):
    return render(request, 'main/recycler_dash.html')

