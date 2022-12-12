from django.shortcuts import render
from chat.models import Post
from .forms import AccountForm
from django.views.generic import View, TemplateView, ListView,CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

#投稿の一覧を表示するビュー
class PostListView(ListView):
    template_name = 'chat/home.html'
    model = Post
    def get_queryset(self):
        if ("order" in self.request.GET):
            if self.request.GET["order"] == "popular":
                return Post.objects.order_by("-fav_num")
            elif self.request.GET["order"] == "new":
                return Post.objects.order_by("-created_at")
            elif self.request.GET["order"] == "veiled":
                return Post.objects.order_by("fav_num")
            elif self.request.GET["order"] == "old":
                return Post.objects.order_by("created_at")
            else:
                return Post.objects.order_by("-created_at")
        return Post.objects.order_by("-created_at")
home = PostListView.as_view()

#Postモデルを使って投稿を作成するビュー
class PostCreateView(CreateView):
    template_name = 'chat/post.html'
    model = Post
    fields = ('author', 'title', 'content')
    success_url = 'http://localhost:8000/home/'

#投稿の詳細を表示するビュー
class PostDetailView(DetailView):
    template_name = "chat/detail.html"
    model = Post

def Login(request):
    if request.method == 'POST':
        # フォーム入力のユーザーID・パスワード取得
        UserName = request.POST.get('username')
        Pass = request.POST.get('password')

        # Djangoの認証機能
        user = authenticate(username=UserName, password=Pass)

        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request, user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('home'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'chat/login.html')


class Logout(LogoutView):
    template_name = "chat/logout.html"
    next_page = "http://localhost:8000/home"

# simple url define
def index(request):
    return render(request, "chat/index.html")
def signup(request):
    return render(request, "chat/signup.html")
#def login(request):
    #return render(request, "chat/login.html")
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
def signupold(request):
    return render(request, "chat/signup-old.html")