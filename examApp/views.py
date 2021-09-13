from django.shortcuts import render
from django.http import HttpResponse
from .models import normal_exam

# Create your views here.
def index(request):
    normal_exams = normal_exam.objects.all()
    n = len(normal_exams)
    params = {'normal_exam':normal_exams}
    return render(request,'exam.html',params)

def demo(request):
    return HttpResponse("This is a  demo")

def submit(request):
    count=0
    normal_exams = normal_exam.objects.all()
    n = len(normal_exams)
    correct = normal_exam.currect_ans
    
    if request.POST.get(f"{correct}_check",'off')=='on':
        count=count+1
    # print(count)
    return HttpResponse(f"{count} out of {n}")
    



