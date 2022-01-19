from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Profile
from .utils import *

class LoginView(APIView):

    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'

        print(request.data.get('username'))
        try:
            print("hello2")
            data = request.data 
            print(data.get('password'))
            print("hello3")
            if data.get('username') is None:
                response['message'] = 'Username not found'
                raise Exception('Username not found')

            if data.get('password') is None:
                response['message'] = 'password not found'
                raise Exception('password not found')

            check_user = User.objects.filter(username = data.get('username')).first()
            if check_user is None:
                response['message'] = 'Invalid Username'
                raise Exception('Invalid Username')

            # if not Profile.objects.filetr(user = check_user).first().is_verified:
            #     response['message'] = 'Your profile is not verified'
            #     raise Exception('Unverified Profile')

            user = authenticate(username = data.get('username'), password = data.get('password'))
            if user:
                login(request, user)
                response['message'] = 'Welcome'
                response['status'] = 200
            else:
                response['message'] = 'Invalid Password'
                raise Exception('Invalid Password')

        except Exception:
            print(Exception)

        return Response(response)

LoginView = LoginView.as_view()

class RegisterView(APIView):

    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something Went Wrong'
        print(request.data)
        try:
            print(request.data)
            data = request.data 
            print(data)
            if data.get('username') is None:
                response['message'] = 'Username Not Found'
                raise Exception('Username Not Found')
            
            if data.get('password') is None:
                response['message'] = 'Password Not Found'
                raise Exception('Password Not Found')

            check_user = User.objects.filter(username = data.get('username')).first() 
            if check_user:
                response['message'] = 'Username Already Taken'
                raise Exception('Username Already Taken')

            # print(request.POST['first_name'])
            # print(request.POST.get('first_name'))
            # print(data.get('last_name'))
            user = User.objects.create(username = data.get('username'), first_name = data.get('first_name'), last_name = data.get('last_name'))
            user.set_password(data.get('password'))
            user.save()

            
            profile  = Profile.objects.create(user = user)
            profile.save()
            login(request, user)

            # token = generate_random_string(20)
            # Profile.objects.create(user = user, token = token)
            # send_mail_to_user(token, data.get('username'))

            response['message'] = 'User Created'
            response['status'] = 200
 
        except Exception:
            print(Exception)

        return Response(response)

RegisterView = RegisterView.as_view()