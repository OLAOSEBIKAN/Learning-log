from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse


def log_out(request):
    logout(request)
    messages.success(request, f"You're logged out!")
    return redirect('index')


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            messages.success(request, f"Your Account has been registered and you're logged in")
            return HttpResponseRedirect(reverse('index'))
    context = {'form': form}
    template = 'users/register.html'
    return render(request, template, context)


