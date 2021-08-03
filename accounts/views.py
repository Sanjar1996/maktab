from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreatForm


class SignUpView(CreateView):
    form_class = CustomUserCreatForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
