from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as auth_login
from home.models import feedback
def index(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    else:
        return redirect('login')



def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')



def verify(request):
    if request.method!='POST':
        # return render(request,'index.html')
        pass
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        # check if user has entered correct credentials
        user = authenticate(request,username=username,password=password)

        if user is not None:
            # A backend authenticated the credentials
            auth_login(request,user)

            messages.success(request,'signed in successfully!')
            return redirect('/')
        else:
            messages.error(request,'please enter correct credentials')
            return render(request,'login.html')
        

def newuser(request):
     if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        data={'first_name' :fname , 'last_name':lname}
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if checkDuplicates(username):
            user=User.objects.create_user(username=username,email=email,password=password,**data)
            user.save()
            messages.success(request,'account created successfully!')
        else:
            messages.error(request,f'username:{username} already exists')
            return redirect('register')
        # if checkPasswordRequirement(password):
        #     pass
        return redirect('login')
    
     else:
        return render(request,'register.html')
     

def savefeedback(request):
    text=request.POST.get('text')
    fname=request.user.first_name
    lname=request.user.last_name
    query=feedback(fname=fname,lname=lname,text=text)
    query.save()
    messages.success(request,'FeedBack Submitted!')
    return redirect('/')





def checkDuplicates(username):
    query=User.objects.filter(username=username)
    if query:
        return False
    else: return True



# def checkPasswordRequirements(password):
#     if len(password)<8:
#         return False