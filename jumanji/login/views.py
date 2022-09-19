from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from login.forms import RegisterUserForm, LoginUserForm


class RegisterUserView(CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'login/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return reverse_lazy('index')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUserView(LoginView):
    model = User
    form_class = LoginUserForm
    template_name = 'login/login.html'


class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'login/profile.html'
    model = User
    form_class = RegisterUserForm
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.id != int(kwargs['pk']):
            return redirect('profile', pk=self.request.user.id)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile', pk=self.request.user.id)
