from rest_framework.generics import UpdateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView

from base.models import User

import datetime

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
import jwt
from django.conf import settings
from django.shortcuts import render

# Create your views here.
base_url = "http://127.0.0.1:8000"


def home(request):
    return render(request, 'home.html')


class SignupAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginAPIView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, settings.SECRET_KEY,
                           algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutAPIView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response


class ListUserAPIView(ListAPIView):
    """This endpoint list all of the available User from the database"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UpdateUserAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific User by passing in the id of the User to update"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DeleteUserAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific User from the database"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetriveUserAPIView(RetrieveAPIView):
    """This endpoint allows to get a specific User from the database"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
