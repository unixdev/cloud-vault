from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, FormView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import SignupForm, VerificationForm
from .models import Document

from logging import getLogger

logger = getLogger('vault.core')


class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'core/signup.html'
    success_url = reverse_lazy('core:verify')

    def form_valid(self, form):
        user = form.save(commit=False)
        logger.info('submitted signup form with phone: %s', user.phone)
        user.is_active = False
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('core:verify', args=[self.object.phone])


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


class VerificationView(FormView):
    form_class = VerificationForm
    template_name = 'core/verification.html'
    success_url = reverse_lazy('core:signup_success')

    def get_initial(self):
        initial = super().get_initial()
        initial.update({
            'phone': self.kwargs['phone']
        })
        return initial

    def form_valid(self, form):
        form.activate_user()
        return super().form_valid(form)


class DocumentCreateView(CreateView):
    model = Document
    fields = ('file', 'note')
    success_url = reverse_lazy('core:list')

    def form_valid(self, form):
        document = form.save(commit=False)
        document.user = self.request.user
        return super().form_valid(form)


class DocumentListView(ListView):
    model = Document

    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(user=user).order_by('created_at')

