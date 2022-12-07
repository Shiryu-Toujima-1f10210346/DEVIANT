from django.shortcuts import render
from chat.models import Post
from django.views.generic import View, TemplateView, ListView,CreateView, DetailView

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
            else:
                return Post.objects.order_by("-created_at")
        return Post.objects.order_by("-created_at")
home = PostListView.as_view()

#Postモデルを使って投稿を作成するビュー
class PostCreateView(CreateView):
    template_name = 'chat/post.html'
    model = Post
    fields = ('author', 'title', 'content')
    success_url = '/home/'
post = PostCreateView.as_view()

#投稿の詳細を表示するビュー
class PostDetailView(DetailView):
    template_name = "chat/detail.html"
    model = Post
detail = PostDetailView.as_view()

# simple url define
def index(request):
    return render(request, "chat/index.html")
def signup(request):
    return render(request, "chat/signup.html")
def login(request):
    return render(request, "chat/login.html")
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