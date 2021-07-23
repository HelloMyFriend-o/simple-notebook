from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView


class RegisterUser(CreateView):
    """User registration."""
    form_class = UserCreationForm
    template_name = 'authorization/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    """User login."""
    form_class = AuthenticationForm
    template_name = 'authorization/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    """User logout."""
    logout(request)
    return redirect('login')
