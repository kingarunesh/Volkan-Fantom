from django.urls import path
from users.views import *
from django.contrib.auth import views as authView


app_name = "users"

urlpatterns = [
    path("", UserListView.as_view(), name="users_list"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("password-change/", authView.PasswordChangeView.as_view(), name="password_change"),
    path("password-change-done/", authView.PasswordChangeDoneView.as_view(), name="password_change_done"),
    path("update-profile/<slug:slug>/", UserUpdateProfileView.as_view(), name="update_profile"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("posts/<int:pk>/", UserPostView.as_view(), name="user_posts")
]