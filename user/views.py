from django.shortcuts import render
from .forms import CreateUserForm
from .models import UserModel
from django.shortcuts import render, redirect
# Create your views here.
#홈페이지
def home(request):
    user = request.user.is_authenticated
    if user:# 로그인 상태
        return redirect('log-in')
    else:
        return redirect('log-in')

def create_user_view(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():  # 2
            print("work")
            username = request.POST.get('username', '')
            email = request.POST.get('email', '')
            password1 = request.POST.get('password_check1', '')
            password2 = request.POST.get('password_check2', '')

            if password1 ==password2:
                UserModel.objects.create_user(username=username,password=password1,email=email)
        else:
            print(form.errors)
    else:
        pass
    form = CreateUserForm()
    return render(request, 'user/create_user.html', {'form': form})  # 4


def log_in_view(request):
    return render(request, 'user/log_in.html')




