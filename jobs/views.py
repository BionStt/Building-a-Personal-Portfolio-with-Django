from django.shortcuts import render,get_object_or_404
from .models import Job

def home(request):
    jobs = Job.objects
    return render(request,'jobs/home.html',{'jobs':jobs})

def blog(request):
    jobs = Job.objects.all()
    return render(request,'jobs/blog_new.html',{'jobs':jobs})

def detail(request,id):
    job_detail = get_object_or_404(Job,pk=id)
    return render(request,'jobs/detail.html',{'job':job_detail})

def test_home(request):
    return render(request,'jobs/home.html')

def test_blog(request):
    return render(request,'jobs/blog.html')
