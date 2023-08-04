from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from apps.user.models import ClienteProfile,ContadorProfile
from apps.catalogo_cuentas.models import Country
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
            if ClienteProfile.objects.filter(user_id=user.id).exists():
                cliente = ClienteProfile.objects.get(user_id=user.id)
                id = str(cliente.cliente_id)
                return redirect("/?id="+id+"&profile=cliente")
            elif ContadorProfile.objects.filter(user_id=user.id).exists():
                contador = ContadorProfile.objects.get(user_id=user.id)
                id = str(contador.contador_id) 
                return redirect("/?id="+id+"&profile=contador")

            return redirect("/")
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
                return redirect('/register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('/register/')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                type_user = request.POST['type_user']
                country = request.POST['country_id']
                print(country)
                user.save()
                id = ""
                if type_user == 'cliente':
                    cliente = ClienteProfile.objects.create(user_id=user.id,name=username,email=email,phone_number=0,country_id=country)
                    id = str(cliente.cliente_id)
                else:
                    contador = ContadorProfile.objects.create(user_id=user.id,name=username,email=email,phone_number=0,country_id=country)
                    id = str(contador.contador_id)
                userAuth = auth.authenticate(username=username,password=password1)
                auth.login(request,userAuth)
                return redirect('/?id='+id+"&profile="+type_user)
        
        else:
            messages.info(request,'password not matching..')    
            return redirect('/register/')
        return redirect('/')

    else:
        queryset = Country.objects.all()
        context = {
            'country':queryset
            }

        return render(request,'register.html',context)



def logout(request):
    auth.logout(request)
    return redirect('/')       