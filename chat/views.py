from django.shortcuts import render
from chat.models import Post, Account
from .forms import AccountForm
from django.views.generic import View, TemplateView, ListView,CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
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

class  AccountRegistration(TemplateView):

    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": AccountForm(),
        }

    # Get処理
    def get(self,request):
        self.params["account_form"] = AccountForm()
        self.params["AccountCreate"] = False
        return render(request,"chat/signup.html",context=self.params)

    # Post処理
    def post(self,request):
        self.params["account_form"] = AccountForm(data=request.POST)

        # フォーム入力の有効検証
        if self.params["account_form"].is_valid():
            # アカウント情報をDB保存
            account = self.params["account_form"].save()
            # パスワードをハッシュ化
            account.set_password(account.password)
            # ハッシュ化パスワード更新
            account.save()

            # 画像アップロード有無検証
            #if 'account_image' in request.FILES:
            #    add_account.account_image = request.FILES['account_image']
            # アカウント作成情報更新
            self.params["AccountCreate"] = True
            # 成功したら自動でログインし､ホームページへ遷移
            login(request, account)
            return HttpResponseRedirect(reverse('home'))

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)

        return render(request,"chat/signup.html",context=self.params)


class Logout(LogoutView):
    template_name = "chat/logout.html"
    next_page = "http://localhost:8000/home"

# simple url define
def index(request):
    return render(request, "chat/index.html")
#def signup(request):
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