from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.AccountRegistration.as_view(), name="singup"),
    path("signupold/", views.signupold, name="singup"),
    path("login/", views.Login, name="login"),
    #path("login/", views.Login.as_view(), name="login"),
    path("home/", views.home, name="home"), 
    path("others_prof/", views.others_prof, name="others_prof"),
    path("home/post/<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("my_prof/", views.MyPostListView.as_view(), name="my_prof"),
    path("post/", views.PostCreateView.as_view(), name="post"),
    path("tos/", views.tos, name="tos"),
    path("forgotpass/", views.forgotpass, name="forgotpass"),
    path("chat/", views.chat, name="chat"),
    path("chat/<str:room_name>/", views.room, name="room"),
    path("logout/", views.Logout.as_view(), name="logout"),
]