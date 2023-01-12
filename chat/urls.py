from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path
urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.AccountRegistration.as_view(), name="signup"),
    path("signupold/", views.signupold, name="singup"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),

    path("home/", views.PostListView.as_view(), name="home"), 
    path("others_prof/", views.others_prof, name="others_prof"),
    path("my_prof/", views.MyPostListView.as_view(), name="my_prof"),
    path("post/", views.PostCreateView.as_view(), name="post"),
    path("tos/", views.tos, name="tos"),
    path("forgotpass/", views.forgotpass, name="forgotpass"),
    path("favlist/", views.FavListView.as_view(), name="favlist"),


    path("chat/", views.chat, name="chat"),
    path("chat/<str:room_name>/", views.room, name="room"),
    


    path("post/<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("post/<int:pk>/comment/", views.CommentCreateView.as_view(), name="comment"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="delete"),
    path("post/<int:pk>/fav/", views.FavView.as_view(), name="fav"),
    path("post/<int:pk>/edit/", views.PostEditView.as_view(), name="edit"),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]