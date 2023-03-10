from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('signup_success/', views.signup_success, name='signup_success'),
    path('login/', views.VaultLoginView.as_view(), name='login'),
    path('logout/', views.VaultLogoutView.as_view(), name='logout'),
    path('verify/<str:phone>/', views.VerificationView.as_view(), name='verify'),
    path('documents/upload', views.DocumentCreateView.as_view(), name='upload'),
    path('documents/', views.DocumentListView.as_view(), name='list'),
    path('downloads/<str:filename>', views.download, name='downloads'),
    path('home/', views.home, name='home'),
]
