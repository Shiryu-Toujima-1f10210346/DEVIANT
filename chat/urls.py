from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.AccountRegistration.as_view(), name="singup"),
    path("signupold/", views.signupold, name="singup"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),

    path("home/", views.PostListView.as_view(), name="home"), 
    path("others_prof/", views.others_prof, name="others_prof"),
    path("my_prof/", views.MyPostListView.as_view(), name="my_prof"),
    path("post/", views.PostCreateView.as_view(), name="post"),
    path("tos/", views.tos, name="tos"),
    path("forgotpass/", views.forgotpass, name="forgotpass"),

    path("chat/", views.chat, name="chat"),
    path("chat/<str:room_name>/", views.room, name="room"),
    


    path("post/<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("post/<int:pk>/comment/", views.CommentCreateView.as_view(), name="comment"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="delete"),
    path("post/<int:pk>/fav/", views.FavView.as_view(), name="fav"),

    # 実装しろ
    # はい･･･
    # path("post/<int:pk>/unfav/", views.unfav, name="unfav"),
    # path("post/<int:pk>/favlist/", views.favlist, name="favlist"),
    path("post/<int:pk>/edit/", views.PostEditView.as_view(), name="edit"),
    ]