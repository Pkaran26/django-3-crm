from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product, name='products'),
    path('customer/<int:pk>/', views.customer, name='customer'),
    path('create_order/<int:pk>/', views.create_order, name='create_order'),
    path('update_order/<int:pk>/', views.update_order, name='update_order'),
    path('delete_order/<int:pk>/', views.delete_order, name='delete_order'),

    path('user/', views.userPage, name='user_page'),
    path('account/', views.account_settings, name='account'),

    path('login/', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),

    path('reset_password', auth_views.PasswordResetView.as_view(template_name="accounts/reset_password.html"), name="reset_password"),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name="password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), name="password_reset_complete"),
]
