from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from apps.user.models import ClienteProfile
# Create your views here.

def loginUser(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        print(user)
        print("USER CONUT")
        if user is not None:
            auth.login(request, user)
            user = ClienteProfile.objects.get(user_id=user.id)
            id=str(user.cliente_id)
            return redirect("/?id="+id)
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')    

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register/')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                userAuth = auth.authenticate(username=username,password=password1)
                auth.login(request,userAuth)
                return redirect('/')
        
        else:
            messages.info(request,'password not matching..')    
            return redirect('register/')
        return redirect('/')
        
    else:
        return render(request,'register.html')



def logout(request):
    auth.logout(request)
    return redirect('/')       