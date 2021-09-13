from django.shortcuts import render
import os
from django.http import HttpResponse
from .models import pdf
from math import ceil


# Create your views here.
def index(request):
    pdfs = pdf.objects.all()
    # print(pdfs)
    n= len(pdfs)
    nSildes = n//4 +ceil((n/4) -(n//4))

    params = {'no_of_slides':nSildes,'range':range(1,nSildes),'pdf':pdfs}
    return render(request,'studyMaterial.html',params)

def visit(request):
    return render(request,'index.html')

