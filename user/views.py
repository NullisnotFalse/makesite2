from django.shortcuts import render

# Create your views here.
def create_user_view(request):
    return render(request, 'user/create_user.html')