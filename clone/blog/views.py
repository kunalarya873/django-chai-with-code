from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base.html')
def login(request):
    return render(request, 'auth/signin.html')
def register(request):
    return render(request, 'auth/register.html')