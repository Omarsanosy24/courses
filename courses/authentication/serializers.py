from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import User
from django_session_jwt.middleware.session import SessionMiddleware
from django.contrib import auth
import json
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'phone', ]

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')



        if not username.isalnum():
            raise serializers.ValidationError('The username should only contain alphanumeric character')
        return attrs

    def create(self, validated_data):

        return User.objects.create_user(**validated_data)

class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=5555555555555555555)

    class Meta:
        model = User
        fields = ['token']


class LoginSerializer(serializers.ModelSerializer):
    email= serializers.EmailField(max_length=2000, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(max_length=2000, min_length=3, read_only=True)
    accessTokens = serializers.CharField(max_length=200000, min_length=6, read_only=True)
    refreshTokens = serializers.CharField(max_length=200000, min_length=6, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'accessTokens', 'id','refreshTokens']

    def validate(self, attrs):
        email=attrs.get('email','')
        password=attrs.get('password','')
        try:
            user = auth.authenticate(email= email, password= password)
 
            if not user:
                raise AuthenticationFailed('Invalid credentials, try again')
            uu = User.objects.get(email = email)
            black = OutstandingToken.objects.filter(user = uu)
            #for i in black:
             #   if i in BlacklistedToken.objects.all():
              #      print('omar')
               # else:
                #    raise AuthenticationFailed('الحساب مستخدم من قبل شخص اخر')

            for i in black:
                BlacklistedToken.objects.get_or_create(token = i)
                print("oooo")
            user = auth.authenticate(email= email, password= password)
 
            if not user.is_verified:
                raise AuthenticationFailed('email is not verified')


            if not user.is_active:
                raise AuthenticationFailed('الحساب مغلق، اتصل بالمالك')

            return {
                'email':user.email,
                'username': user.username,
                'accessTokens':RefreshToken.access_token_class.for_user(user),
                'refreshTokens':RefreshToken.for_user(user),
            }
            return super().validate(attrs)

        except:
            user = auth.authenticate(email= email, password= password)
 
            if not user:
                raise AuthenticationFailed('Invalid credentials, try again')
            uu = User.objects.get(email = email)
            black = OutstandingToken.objects.filter(user = uu)
            #for i in black:
             #   if i in BlacklistedToken.objects.all():
              #      print('omar')
               # else:
                #    raise AuthenticationFailed('الحساب مستخدم من قبل شخص اخر')

            for i in black:
                BlacklistedToken.objects.get_or_create(token = i)
                print("oooo")
            user = auth.authenticate(email= email, password= password)
 
            if not user.is_verified:
                raise AuthenticationFailed('email is not verified')


            if not user.is_active:
                raise AuthenticationFailed('الحساب مغلق، اتصل بالمالك')

            return {
                'email':user.email,
                'username': user.username,
                'accessTokens':RefreshToken.access_token_class.for_user(user),
                'refreshTokens':RefreshToken.for_user(user),
            }
            return super().validate(attrs)


class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)


    class Meta:
        fields = ['email']


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(
        min_length=1, write_only=True)
    uidb64 = serializers.CharField(
        min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid', 401)

            user.set_password(password)
            user.save()

            return (user)
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)
        return super().validate(attrs)


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')
        

