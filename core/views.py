from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import SignupForm


class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'core/signup.html'
    success_url = reverse_lazy('core:signup_success')


def signup_success(request):
    context = {
        'login_url': reverse('core:login')
    }

    return render(request, 'core/signup_success.html', context)


class VaultLoginView(LoginView):
    template_name = 'core/login.html'


class VaultLogoutView(LogoutView):
    template_name = 'core/logout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'login_url': reverse('core:login')
        })
        return context


def home(request):
    context = {
        'user': request.user,
        'logout_url': reverse('core:logout'),
    }

    return render(request, 'core/home.html', context)


def landing(request):
    context = {
        'login_url': reverse('core:login'),
        'signup_url': reverse('core:signup'),
    }

    return render(request, 'core/landing.html', context)
