from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from p_library.forms import AuthorForm

# Create your views here.


class Start(ListView):
    template_name = 'start.html'
    queryset = {}

    # def dispatch(self, request, *args, **kwargs):
    #     print(request.user.is_authenticated)
    #     return HttpResponse(render(request,'start.html'))
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(*kwargs)
        if self.request.user.is_authenticated:
            context['username'] = self.request.user.username
            # context['social_account'] = SocialAccount.objects.get(provider='github', user=self.request.user)
            return context


# def Start(request):
#     context = {}
#     if request.user.is_authenticated:
#         context['username'] = request.user.username
#         context['social_account'] = SocialAccount.objects.get(provider='github', user=request.user)
#         print(context['social_account'].extra_data)
#     return render(request, 'start.html', context )

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
    form_class = AuthorForm
    template_name = 'create-profile.html'

    def form_valid(self, form):
        print(dir(form))
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(*kwargs)
    #     # json_data = {
    #     #     'name': self.request
    #     # }
    #     print(dir(self.request))
    #     # new_user = SocialAccount.objects.create(provider='custom', user=self.request.user)
    #     return context

