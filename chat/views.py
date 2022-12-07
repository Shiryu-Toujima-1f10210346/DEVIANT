from django.shortcuts import render
from chat.models import Post
from django.views.generic import View, TemplateView, ListView,CreateView, DetailView

#投稿の一覧を表示するビュー
class PostListView(ListView):
    template_name = 'chat/home.html'
    model = Post
home = PostListView.as_view()

#Postモデルを使って投稿を作成するビュー
class PostCreateView(CreateView):
    template_name = 'chat/post.html'
    model = Post
    fields = ('author', 'title', 'content')
    success_url = '/home/'
post = PostCreateView.as_view()
# simple url define
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
def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})