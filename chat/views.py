from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "chat/index.html")
def signup(request):
    return render(request, "chat/signup.html")
def login(request):
    return render(request, "chat/login.html")
def home(request):
    return render(request, "chat/home.html")
def others_prof(request):
    return render(request, "chat/others_prof.html")
def my_prof(request):
    return render(request, "chat/my_prof.html")
def post(request):
    return render(request, "chat/post.html")
def tos(request):
    return render(request, "chat/tos.html")
def forgotpass(request):
    return render(request, "chat/forgotpass.html")
def chat(request):
    return render(request, "chat/chat.html")