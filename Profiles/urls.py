from django.urls import path
from .views import (
    login_to_profile,
)

app_name = 'Profiles'

urlpatterns = [
    path('', login_to_profile, name='login')
]