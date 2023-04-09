from django.shortcuts import render
from .forms import CreateUserForm
from .models import UserModel
# Create your views here.
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