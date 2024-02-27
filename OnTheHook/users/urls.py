from django.contrib.auth import views as djangoviews
from django.contrib.auth.decorators import login_required
from django.urls import path

import users.views as views

app_name = "users"

urlpatterns = [
    path(
        "profile/",
        login_required(views.ProfileView.as_view()),
        name="profile",
    ),
    path(
        "register/",
        views.RegisterView.as_view(),
        name="register",
    ),
    path(
        "login/",
        djangoviews.LoginView.as_view(
            template_name="users/auth/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path(
        "logout/",
        djangoviews.LogoutView.as_view(
            template_name="users/auth/logout.html",
        ),
        name="logout",
    ),
    path(
        "password_change/",
        djangoviews.PasswordChangeView.as_view(
            template_name="users/auth/password_change.html",
        ),
        name="change_password",
    ),
    path(
        "password_change/done/",
        djangoviews.PasswordChangeDoneView.as_view(
            template_name="users/auth/password_change_done.html",
        ),
        name="password_change_done",
    ),
    path(
        "password_reset/",
        djangoviews.PasswordResetView.as_view(
            template_name="users/auth/password_reset.html",
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        djangoviews.PasswordResetDoneView.as_view(
            template_name="users/auth/password_reset_done.html",
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        djangoviews.PasswordResetConfirmView.as_view(
            template_name="users/auth/password_reset_confirm.html",
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        djangoviews.PasswordResetCompleteView.as_view(
            template_name="users/auth/password_reset_complete.html",
        ),
        name="password_reset_complete",
    ),
]
