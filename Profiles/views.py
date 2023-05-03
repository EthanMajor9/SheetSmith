from django.shortcuts import render
from .forms import LoginForm

# Create your views here.
def login_to_profile(request):
    login_form = LoginForm()
    return render(request, 'Profiles/login.html', {'form': login_form})