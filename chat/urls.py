from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="singup"),
    path("signupold/", views.signupold, name="singup"),
    path("login/", views.login, name="login"),
    #path("home/", views.home, name="home"),
    path("home/", views.home, name="home"), 
    path("others_prof/", views.others_prof, name="others_prof"),
    path("home/post/<int:pk>/", views.detail, name="detail"),
    path("my_prof/", views.my_prof, name="my_prof"),
    path("post/", views.post, name="post"),
    path("tos/", views.tos, name="tos"),
    path("forgotpass/", views.forgotpass, name="forgotpass"),
    path("chat/", views.chat, name="chat"),
    path("chat/<str:room_name>/", views.room, name="room"),
]