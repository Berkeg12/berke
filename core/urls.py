from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Post işlemleri
    path('', views.post_list, name='post_list'),
    path('add/', views.post_create, name='post_create'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/edit/', views.post_update, name='post_update'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),

    # Kullanıcı kimlik doğrulama işlemleri
    # Kullanıcı kimlik doğrulama işlemleri
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),


    # Şifre sıfırlama işlemleri
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

    # Profil düzenleme (önce gelmeli!)
    path('profile/edit/', views.edit_profile, name='edit_profile'),

    # Profil görüntüleme
    path('profile/<str:username>/', views.profile_detail, name='profile_detail'),
]



