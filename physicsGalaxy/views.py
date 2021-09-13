
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
import datetime
from contactData.models import product
from examApp.models import normal_exam
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def index(request):
    return render(request,'index.html')


def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def send_data(request):
    name1= request.POST.get('name','none')
    email1 = request.POST.get('email','none')
    comments1 = request.POST.get('textArea','none')
    print(name1)
    print(email1)
    print(comments1)
    
    data = datetime.datetime.now()
    data= str(data).split(" ")
    product.objects.create(name=name1, email=email1, date= data[0], comments=comments1)
    return render(request, 'contact.html')

def index1(request):
    	return render(request, 'index1.html')

def questions(request):
	return render(request, 'quiz.html')

def login(request):
	return render(request, 'username.html')

def userScore(request):
    pass

def logintoquiz(request):
    return render(request,'logintoquiz.html') 

def getUser(request):
    user = request.POST.get('userName','not_specified')
    return user
def singUp(request):
    return render(request,'SingUp.html')
    
def handleSingUp(request):
    if request.method =="POST":
        # get the parameters
        name = request.POST['user_Name_1']
        print(name)
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST['password1']
        re_password = request.POST['re-password']
        email = request.POST['email']
        institude_code = request.POST['code']

        if  len(name)>20:
            messages.error(request,"User must be under 10 character")
            return redirect('log_in_to_quiz')
        if password != re_password:
            messages.error(request,"Paswword not matched")
            return redirect('log_in_to_quiz')

        if institude_code !="PGS10":
            messages.error(request,"Institute code is invalid!")
            return redirect('log_in_to_quiz')

        if not name.isalnum():
            messages.error(request,"User name should be alphanumeric")
            return redirect('log_in_to_quiz')



        # # create user
        myuser = User.objects.create_user(name,email,password)
        myuser.first_name =fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your account has been created successfully!")
        return redirect('log_in_to_quiz')


    else:
        return HttpResponse("404 -Not Found")

def handleLogIn(request):
    if request.method =="POST":
        # get the parameters
        loginname = request.POST['userName1']
        loginpassword = request.POST['password2']

        user =authenticate(username=loginname,password = loginpassword)
        if user is not None:
            auth_login(request,user)
        
            messages.success(request,"Successfully Logged In !")
            return render(request,"userpage.html")
        else:
            messages.success(request,"Invalid Credentials, Please try again!")
            return redirect("log_in_to_quiz")



    return HttpResponse("Log in here!")

def handleLogOut(request):
    
    auth_logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('log_in_to_quiz')

def userPage(request):
    return render(request,"userpage.html")     

  




    
    


