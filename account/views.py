from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required


# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request,
#                                 username=cd['username'],
#                                 password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authenticated Successfully')
#                 else:
#                     return HttpResponse('Disabled Account')
#             else:
#                 return HttpResponse('Invalid login')

#     else:
#         form = LoginForm()

#     return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


def register(request):
    template = 'account/register.html'
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST or None)
        if user_form.is_valid():
            # Create new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            template = 'account/register_done.html'
            return render(request, template, {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()

    return render(request, template, {'user_form': user_form})
