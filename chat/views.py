from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "chat/index.html")
def signup(request):
    return render(request, "chat/signup.html")
def login(request):
    return render(request, "chat/login.html")