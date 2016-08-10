from django.db import transaction
from django.utils.html import escape
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from rest_framework.generics import CreateAPIView,GenericAPIView,RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from rest_framework.decorators import api_view
from rest_framework.permissions import (
    AllowAny,
)



from .serializers import( UserLogInSerialiser,
                          UserCreateSerializer,
                          UserDetailSerializer,
                          )


from o2o_rest_framwork import settings

from o2o_rest_framwork.permissions.UserPermissions import IsOwner,IsVarified

class UserCreateAPIView(CreateAPIView):

    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        with transaction.atomic():
            instance=serializer.save()
            email=instance.get('email')
            instance = User.objects.get(username=instance.get('username'))
            id = instance.id
            print id
            CONFIRM_URL='http://127.0.0.1:8000/user/confirm/{0}/{1}'
            confirm_url=CONFIRM_URL.format(
                #escape is usesd for ignore '/', actually we don;t need it in here but well...
                escape(email),
                escape(id)
            )
            send_email('email comfirm from our company',confirm_url,email)



def send_email(title,content,*to_suer):
    send_mail(title, content, settings.EMAIL_HOST_USER, to_suer ,fail_silently=False)
    print 1

class UserLogInAPIView(GenericAPIView):

    permission_classes = [AllowAny]
    serializer_class = UserLogInSerialiser

    def post(self,request,*args,**kwargs):
        data = request.data
        serialiser = UserLogInSerialiser(data=data)
        if serialiser.is_valid(raise_exception=True):
            new_data = serialiser.data
            # user = User.user = User.objects.filter(username=new_data['username'])
            user = authenticate(username=new_data.get('username'), password=new_data.get('password'))
            print new_data.get('username'),
            print new_data.get('password'),
            if user is not None:
                login(request,user)
            else:
                print 1
            return Response(new_data,status=HTTP_200_OK)
        return Response(serialiser.errors,status=HTTP_400_BAD_REQUEST)

class UserDetailAPIView(RetrieveAPIView):

    permission_classes = [IsOwner]
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()

class UserVerifyAPIView(GenericAPIView):

    def get(self,request,*args,**kwargs):
        id = kwargs['id']
        email = kwargs['email']
        user_qs =User.objects.filter(id=int(id),email=email)
        if user_qs.exists():
            user = user_qs.first()
            user.is_active = True
            user.save()
            return Response(status=HTTP_200_OK)
        return Response(status=HTTP_400_BAD_REQUEST)

class UserLogoutAPIView(GenericAPIView):
    def get(self,request,*args,**kwargs):
        logout(request)
        return Response(HTTP_200_OK)


