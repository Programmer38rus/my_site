from django.urls import path
from .views import Start, RegisterView, CreateProfile

from django.conf import settings
from django.conf.urls.static import static
app_name = 'authorization'

# for allauth
from allauth.account.views import login, logout

urlpatterns = [
  path('', Start.as_view(), name='start'),
  path('login_github/', login, name='login'),
  path('logout_github/', logout, name='logout'),
  path('registration/', RegisterView.as_view(), name='registration'),
  path('create_profile/', CreateProfile.as_view(), name='create_profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
