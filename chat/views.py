from django.shortcuts import render
from chat.models import Post, Comment, FavoriteList
from .forms import AccountForm, CommentForm
from django.views.generic import View, TemplateView, ListView,CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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
            elif self.request.GET["order"] == "pv":
                return Post.objects.order_by("-pv")
            else:
                return Post.objects.order_by("-created_at")
        return Post.objects.order_by("-created_at")

#お気に入り一覧を表示するビュー
class FavListView(ListView):
    template_name = 'chat/home.html'
    model = Post
    def get_queryset(self):
        fav_list = FavoriteList.objects.filter(user_id=self.request.user.id)
        fav_post = []
        for fav in fav_list:
            fav_post.append(Post.objects.get(pk=fav.post_id))
        return fav_post

#投稿の作成を行うビュー
#authorにアカウントの名前を入れる
#imgが空の場合はNoneを入れ
class PostCreateView(CreateView):
    template_name = 'chat/post.html'
    model = Post
    fields = ('title','sex','looks','type','state','content','img')
    def form_valid(self, form):
        if form.instance.img == "":
            form.instance.img = None
        form.instance.author = self.request.user
        return super().form_valid(form)
    #homeにリダイレクト
    success_url = '/home/'

#投稿の詳細を表示するビュー
#PVを1増やす
class PostDetailView(DetailView):
    template_name = "chat/detail.html"
    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Post.objects.get(pk=self.kwargs['pk'])
        if post.author != self.request.user.username:
            post.pv += 1
            post.save()
        context["comment_form"] = CommentForm()
        context["favorite"] = FavoriteList.objects.filter(user_id=self.request.user.id, post_id=self.kwargs['pk'])
        return context

#コメントを作成するビュー
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    def form_valid(self, form):
        post = Post.objects.get(pk=self.kwargs['pk'])
        post.comment_num += 1
        #リダイレクト時､PVが増えてしまうので-1
        post.pv -= 1
        post.save()
        #post_comment_idにcomment_numを入れる
        form.instance.post_comment_id = post.comment_num
        #comment_idに投稿のidを入れる
        form.instance.comment_id = self.kwargs['pk']
        #usernameにアカウントの名前を入れる 
        form.instance.username = self.request.user
        #textにコメントの内容を入れる
        form.instance.text = form.cleaned_data['text']
        #保存
        form.save()
        return HttpResponseRedirect(reverse('detail', kwargs={'pk': self.kwargs['pk']}))

#自分の投稿を削除するビュー
class PostDeleteView(View):
    def get(self, request, *args, **kwargs):
        #投稿者とログインユーザーが一致しているか確認
        
        post = Post.objects.get(pk=self.kwargs['pk'])
        if post.author == self.request.user.username:
            post.delete()
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponseRedirect(reverse('detail'))

#自分の投稿一覧を表示するビュー
class MyPostListView(ListView):
    template_name = 'chat/home.html'
    model = Post
    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

#自分の投稿を編集するビュー
class PostEditView(View):
    def get(self, request, *args, **kwargs):
        #投稿者とログインユーザーが一致しているか確認
        if Post.objects.get(pk=self.kwargs['pk']).author == self.request.user:
            post = Post.objects.get(pk=self.kwargs['pk'])
            return render(request, 'chat/edit.html', {'post':post})
        else:
            return HttpResponseRedirect(reverse('home'))

    def post(self, request, *args, **kwargs):
        #投稿者とログインユーザーが一致しているか確認
        if Post.objects.get(pk=self.kwargs['pk']).author == self.request.user:
            post = Post.objects.get(pk=self.kwargs['pk'])
            post.title = request.POST['title']
            post.content = request.POST['content']
            post.save()
            return HttpResponseRedirect(reverse('detail', kwargs={'pk': self.kwargs['pk']}))
        else:
            return HttpResponseRedirect(reverse('home'))

#お気に入りにした投稿のfav_numを+1する
#Favoritelistに投稿のidを保存する
#既にお気に入りにしていたらfav_numを-1し､Favoritelistから削除する
class FavView(View):
    def get(self, request, *args, **kwargs):
        post = Post.objects.get(pk=self.kwargs['pk'])
        fav = FavoriteList.objects.filter(post_id=self.kwargs['pk'], user_id=self.request.user.id)
        if fav:
            post.fav_num -= 1
            post.save()
            fav.delete()
            return HttpResponseRedirect(reverse('detail', kwargs={'pk': self.kwargs['pk']}))
        else:
            post.fav_num += 1
            post.save()
            fav = FavoriteList()
            fav.post_id = self.kwargs['pk']
            fav.user_id = self.request.user.id
            fav.save()
            return HttpResponseRedirect(reverse('detail', kwargs={'pk': self.kwargs['pk']}))




############################################
############ログイン･ログアウト処理###########
############################################
#ログイン
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
        #Email重複していないなら
        if not User.objects.filter(email=request.POST.get("email")).exists():
            #チェックボックスがオンになっているか検証
            if request.POST.get("checkbox") != "checked":
                return HttpResponse("利用規約に同意してください")
            else:
                #パスワードが一致しているか検証
                if request.POST.get("password") != request.POST.get("confirm-password"):
                    return HttpResponse("パスワードが一致しません")
                else:
                # フォーム入力の有効検証
                    if not self.params["account_form"].is_valid():
                        print(self.params["account_form"].errors)
                    else:
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
            return HttpResponse("このメールアドレスは既に登録されています")
        return render(request,"chat/signup.html",context=self.params)

class Logout(LogoutView):
    template_name = "chat/logout.html"
    next_page = "home"

# simple url define
def index(request):
    return render(request, "chat/index.html")
def others_prof(request):
    return render(request, "chat/others_prof.html")
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