from django.urls import path
from . import views


urlpatterns = [
    path('api/login', views.LoginAPIView.as_view(), name='loginAPI'),
    path('api/register', views.SignupAPIView.as_view(), name='signupAPI'),
    path('api/logout', views.LogoutAPIView.as_view(), name='logoutAPI'),

    path('api/user', views.UserView.as_view(), name='userAPI'),

    path('api/users', views.ListUserAPIView.as_view(), name='usersList'),
    path('api/delete/<int:pk>', views.DeleteUserAPIView.as_view(), name='delete'),
    path('api/update/<int:pk>', views.UpdateUserAPIView.as_view(), name='update'),
    path('api/retrive/<int:pk>', views.RetriveUserAPIView.as_view(), name='retrive'),

    path('', views.home, name='home'),

]
