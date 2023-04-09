from django.urls import path
from . import views   # user/views 불러오기

urlpatterns = [
    path('', views.home, name='home'),
    path('create-user/', views.create_user_view, name='create-user'),
    path('log-in/', views.log_in_view, name='log-in'),
    path('logout/',views.logout,name='logout')
]