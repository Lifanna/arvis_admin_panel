from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, logout
from account import forms, models


# def login(request):
#     form=forms.LoginForm()
#     msg = []
#     if request.method == 'POST':
#         form=forms.LoginForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 if user.is_active:
#                     if user.is_staff:
#                         print("djhfjhsdfj")
#                         return redirect('choice') 
#                     else:
#                         auth.login(request, user)
#                         msg.append("login successful")
#                         return redirect('home')
#                 else:
#                     msg.append("disabled account")
#             else:
#                 msg.append("invalid login")

#     return render(request, 'account/login.html')
    

# def my_logout(request):
#     logout(request)
#     return redirect('home')


# def register(request):
#     form = forms.CustomUserForm()
#     if request.method == 'POST':
#         print('ddd', request.POST)
#         form = forms.CustomUserForm(request.POST)
#         if form.is_valid():
#             print("fdgdf")
#             user = form.save(commit=False)  
#             user.save()
#             return redirect('login')
#         else:
#             print("xfdds")
#     return render(request, "account/register.html", { 'form': form})

from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    template_name='account/login.html'

    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class CustomRegistrationView(CreateView):
    template_name = "account/registration.html"
    model = models.CustomUser
    form_class = forms.CustomUserRegistrationForm
    success_url = '/account/users'


class UsersListView(ListView):
    model = models.CustomUser
    queryset = models.CustomUser.objects.all()
    template_name = 'main/users_list.html'
    context_object_name = 'users'


class CustomUserUpdateView(UpdateView):
    model = models.CustomUser
    queryset = models.CustomUser.objects.all()
    template_name = 'main/update_user.html'
    form_class = forms.CustomUserUpdateForm
    success_url = '/account/users'


class CustomUserDeleteView(DeleteView):
    model = models.CustomUser
    queryset = models.CustomUser.objects.all()
    template_name = 'main/delete_user.html'
    success_url = '/account/users'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
