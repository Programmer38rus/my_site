from allauth.socialaccount.models import SocialAccount
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, UpdateView, View

from authorization.forms import ProfileCreateForm
from .models import UserProfile


# Create your views here.
def Start(request):
    context = {}
    if request.user.is_authenticated:
        context['username'] = request.user.username
        # context['social_account'] = SocialAccount.objects.get(provider='github', user=request.user)
        # print(context['social_account'].extra_data)
    return render(request, 'start.html', context)


class RegisterView(FormView):
    form_class = UserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('authorization:create_profile')

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')

        login(self.request, authenticate(username=username, password=raw_password))
        return super(RegisterView, self).form_valid(form)


class CreateProfile(FormView):
    form_class = ProfileCreateForm
    template_name = 'create-profile.html'
    success_url = reverse_lazy('authorization:start')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super(CreateProfile, self).form_valid(form)


class UpdateProfile(UpdateView):
    model = UserProfile
    form_class = ProfileCreateForm
    success_url = reverse_lazy('authorization:start')
    template_name = 'profile.html'

def update_profile(request):
    user = SocialAccount.objects.get(provider='github', user_id=request.user)
    if request.method == 'POST':
        user.extra_data['name'] = request.POST['name']
        user.extra_data['age'] = request.POST['age']
        user.extra_data['location'] = request.POST['location']
        user.save()
        return HttpResponseRedirect(reverse_lazy('authorization:start'))
    else:
        context = {'user': user}
        return render(request, 'profile_github.html', context)

