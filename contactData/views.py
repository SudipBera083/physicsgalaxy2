from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
import datetime
from contactData.models import product

# Create your views here.
def index(request):
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
    return render(request, 'index.html')
    


    
    # return HttpResponse("Successfully send!")