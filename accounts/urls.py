from django.urls import path
from django.contrib.auth import views as auth_views

app_name = "accounts"
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Passwords
    path('password-change/', auth_views.PasswordResetView.as_view(), name='login'),
    path('password-change-done/', auth_views.PasswordResetDoneView.as_view(), name='login'),
    path('password-reset/', auth_views.PasswordChangeView.as_view(), name='login'),
    path('password-reset-done/', auth_views.PasswordChangeDoneView.as_view(), name='login'),
    path('password-reset-confirm/', auth_views.PasswordResetConfirmView.as_view(), name='login'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(), name='login'),


]
