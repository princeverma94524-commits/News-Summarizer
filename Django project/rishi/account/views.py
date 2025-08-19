from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

#===================================login_page+++++++++++++++++===============================
def login_page(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=auth.authenticate(request,username=username, password=password)
        
        if user is not None:
            auth.login(request,user)  

            return redirect("dashboard")
        else:
            messages.error(request, "bhai register kar lo ")
       
    

    
    return render(request, 'login.html')
#--------------------register_page ------------------------------------------------------------
def register_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        password=request.POST.get("password")
#-----------here user model ka use kiya hai like django give this already ---------------------        
        new_user=User.objects.create_user (
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

        new_user.set_password(password)# Setting the password for the new user in an encrypted 
        new_user.save()
        return redirect("home")
    
    return render(request,'register.html')