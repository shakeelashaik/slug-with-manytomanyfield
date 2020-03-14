from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib.auth.models import User
from .forms import ReqForm
from .models import Reqdata, Reqtype, State, Status, Profile
from django.contrib import messages
from django.utils.text import slugify

# Create your views here.


def index(request):
    return render(request, 'index.html')


def main(request):
    if request.method == "POST":
        form = ReqForm(request.POST or {})
        
        if form.is_valid():
            data_obj = form.save()
            # data_obj.user = request.user
            data_obj.save()
            slug_str = ''
            for req in data_obj.Requesttype.all():
                if slug_str == '':
                    slug_str += req.typ                
                else:
                    slug_str += '-'+req.typ
            slug = slugify(slug_str)
            qs_exists = Reqdata.objects.filter(slug=slug).exists()
            if qs_exists:
                slug = slug+str(data_obj.id)
            data_obj.slug = slug
            data_obj.save()

            return redirect('table')
        else:
            form = ReqForm()
            return render(request, 'main.html', {'form': form})    
    else:
        form = ReqForm()
        return render(request, "main.html", {'form': form, 'viewtab': 'main', 'slug': None})


def table(request):
    tab = Reqdata.objects.all()
    return render(request, 'table.html', {'d': tab})


def viewpage(request,slug):
    vie=Reqdata.objects.get(slug=slug)
    return render(request, 'viewpage.html', {'a': vie})


def registerpage(request):
    return render(request,'register.html')


def register(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirmpass']
        if password1 == password2:

            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists")
                return render(request, 'index.html')
            else:

                user = User.objects.create_user(username=email, email=email, password=password1)
                Profile.objects.create(user=user, phone=phone)
                user = authenticate(username=email, password=password1)
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                if user:
                    messages.success(request, "Registered successfully")
                    return redirect(table)
        else:
            return render(request, 'index.html')
    else:
        return render(request, 'index.html') 


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user= auth.authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login successfull")
            return redirect(table)
        else:
            messages.error(request, "Invalid credentials")
            return render(request, 'index.html')
    else:
        return redirect(login)


def logout(request):
    auth_logout(request)
    return redirect('/')           