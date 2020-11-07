# from django.contrib.auth import login
from django.contrib.auth.views import LoginView as login
from django.urls import path
from .views import Start, RegisterView, CreateProfile, update_profile, UpdateProfile

from django.conf import settings
from django.conf.urls.static import static
app_name = 'authorization'

# for allauth
from allauth.account.views import (
  login as login_github,
  logout as logout_github,
)

urlpatterns = [
  path('', Start, name='start'),
  path('login/', login.as_view(template_name='login.html'), name='login'),
  path('login_github/', login_github, name='login_git'),
  path('logout_github/', logout_github, name='logout_git'),
  path('registration/', RegisterView.as_view(), name='registration'),
  path('create_profile/', CreateProfile.as_view(), name='create_profile'),
  path('profile/<int:pk>/', UpdateProfile.as_view(), name='profile'),
  path('profile_git/', update_profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
