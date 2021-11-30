from django.shortcuts import render

# Create your views here.

def index(request):
    return render (request, 'etudiant/index.html')

def login(request):
    return render(request, 'etudiant/login.html')

def about(request):
    return render(request, 'etudiant/about.html')

def course(request):
    return render(request, 'etudiant/course.html')

def contact(request):
    return render(request, 'etudiant/contact.html')

def event(request):
    return render(request, 'etudiant/event.html')