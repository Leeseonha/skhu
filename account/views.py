from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import LoginForm, UserForm
from .models import User
# from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import auth
from django.http import HttpResponse

# Create your views here.
def layout(request):
    return render(request, 'account/layout.html')

def index(request):
    users = User.objects
    return render(request, 'account/index.html')

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('account:index')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'account/signin.html', {'form':form})

def logout(request):
    auth.logout(request)
    return render(request, 'account/layout.html')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(username=form.cleaned_data["username"],student_id=form.cleaned_data["student_id"],major=form.cleaned_data["major"],grade=form.cleaned_data["grade"],phone_number=form.cleaned_data["phone_number"],password=form.cleaned_data["password"])
            login(request, new_user)
            return redirect('account:index')
    else:
        form = UserForm()
        return render(request, 'account/signup.html', {'form':form})