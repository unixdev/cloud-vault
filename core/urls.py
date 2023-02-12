from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('signup_success/', views.signup_success, name='signup_success'),
    path('login/', views.VaultLoginView.as_view(), name='login'),
    path('logout/', views.VaultLogoutView.as_view(), name='logout'),
    path('verify/', views.VerificationView.as_view(), name='verify'),
    path('home/', views.home, name='home'),
]
