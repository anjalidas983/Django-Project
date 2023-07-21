from django.shortcuts import render,redirect
from .models import Category,Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
         category_data=Category.objects.all()
         return render(request,"category.html",{"datas":category_data})
@login_required
def product_detail(request,p):
    category_type=Category.objects.get(slug=p)
    product_data=Product.objects.filter(category__slug=p)
    return  render(request,"product_details.html",{'product_datas':product_data,'category_type':category_type})
@login_required
def products_data(request,p):
    pr=Product.objects.get(slug=p)
    return render(request,"products.html",{'p_data':pr})

def signup(request):
    if(request.method=="POST"):
            u=request.POST['u']
            p=request.POST['p']
            cp=request.POST['cp']
            e=request.POST['e']
            f=request.POST['f']
            l=request.POST['l']
            if(p==cp):
                u=User.objects.create_user(username=u,
                                           password=p,
                                           email=e,
                                           first_name=f,
                                           last_name=l)
                u.save()
                return redirect('shop:home')
            else:
                messages.error(request,"PASSWORDS ARE NOT SAME")
    return render(request,'signup.html')

def user_login(request):
    if(request.method=="POST"):
        username = request.POST['u']
        password = request.POST['p']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('shop:home')
        else:
            messages.error(request,"Invalid User Credentials")

    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('shop:home')
