from django.urls import path
from . import views


urlpatterns = [
    path('login', views.LoginAPIView.as_view(), name='loginAPI'),
    path('register', views.SignupAPIView.as_view(), name='signupAPI'),
    path('logout', views.LogoutAPIView.as_view(), name='logoutAPI'),

    path('user', views.UserView.as_view(), name='userAPI'),

    path('users', views.ListUserAPIView.as_view(), name='usersList'),
    path('delete/<int:pk>', views.DeleteUserAPIView.as_view(), name='delete'),
    path('update/<int:pk>', views.UpdateUserAPIView.as_view(), name='update'),
    path('retrive/<int:pk>', views.RetriveUserAPIView.as_view(), name='retrive'),
]
