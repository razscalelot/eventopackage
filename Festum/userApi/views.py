from django.db import connection
import razorpay
from ast import Num
from django.db.models import manager
from django.utils.safestring import mark_safe
from django.shortcuts import render
import json

from django.contrib.auth.backends import ModelBackend
from django.core.mail import send_mail

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django.http.response import JsonResponse

from rest_framework.views import APIView
from sqlalchemy import false
from userApi.decorater import allowuser

from userApi.models import *
from userApi.serializers import *

from userApi.utils import generateOTP

from userApi.environ import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
from twilio.rest import Client

from userApi.chatterbot import bot

import userApi.FCMmanager as fcm

import datetime


def createUser(serializeruser):
    print('serializeruser', serializeruser)
    register = serializeruser
    data = {}
    if register.is_valid():
        account = register.save()
        data['response'] = "Successfully registered a new user"
        data['email'] = account.email
        data['phone_no'] = account.phone_no
        token = Token.objects.get(user=account).key
        data['token'] = token

        data = register.data
        refercode = data['refer_code']
        if refercode != None:
            user = User.objects.all()
            regs_serializer = RegistrationSerializer(user, many=True)
            d = regs_serializer.data
            for i in d:
                existing_refer = i['users_ref_code']
                if refercode == existing_refer:
                    user = User.objects.filter(
                        users_ref_code=refercode).first()

                    user.coins = int(user.coins) + int(20)
                    user.save()
                    newuser = User.objects.filter(
                        refer_code=refercode).last()
                    newuser.coins = int(newuser.coins) + int(10)
                    newuser.save()
                    user_data = User.objects.filter().last()
                    serialize = RegistrationSerializer(user_data)
                    data = serialize.data
                    userId = data['userId']
                    name = data['name']

                    value = {
                        "user": userId,
                        "img": "http://eventopackage.com/static/media/LoginRefer.png",
                        "translation_type": "Login Refer",
                        "details": name,
                        "Amount": 10
                    }
                    transaction_serializer = TransactionsSerializer(
                        data=value)
                    if transaction_serializer.is_valid():
                        transaction_serializer.save()
                    value = {
                        "user": user.userId,
                        "img": "http://eventopackage.com/static/media/LoginRefer.png",
                        "translation_type": "Login Refer",
                        "details": user.name,
                        "Amount": 20
                    }
                    transaction_serializer = TransactionsSerializer(
                        data=value)
                    if transaction_serializer.is_valid():
                        transaction_serializer.save()

        return True
    else:
        return register.errors


@api_view(['POST', ])
def adminRegistration(request):
    if request.method == 'POST':
        print('call')
        if request.data.get("refer_code") is None:
            request.data["refer_code"] = ""
        print('request.data', request.data)
        user = createUser(AdminRegistrationSerializer(data=request.data))
        print('user', user)
        if user == True:
            return JsonResponse({
                'message': "Register successfully",
                'data': 1,
                'isSuccess': True
            }, status=201)
        else:
            return JsonResponse({
                'message': "Registration faild",
                'data': user,
                'isSuccess': False
            })


@api_view(['POST', ])
def subAdminRegistration(request):
    if request.method == 'POST':
        print('call')
        if request.data.get("refer_code") is None:
            request.data["refer_code"] = ""
        print('request.data', request.data)
        user = createUser(SubAdminRegistrationSerializer(data=request.data))
        print('user', user)
        if user == True:
            return JsonResponse({
                'message': "Register successfully",
                'data': 1,
                'isSuccess': True
            }, status=201)
        else:
            return JsonResponse({
                'message': "Registration faild",
                'data': user,
                'isSuccess': False
            })


@api_view(['POST', ])
def organizerRegistration(request):
    if request.method == 'POST':
        print('call')
        if request.data.get("refer_code") is None:
            request.data["refer_code"] = ""
        print('request.data', request.data)
        user = createUser(OrganizerRegistrationSerializer(data=request.data))
        print('user', user)
        if user == True:
            return JsonResponse({
                'message': "Register successfully",
                'data': 1,
                'isSuccess': True
            }, status=201)
        else:
            return JsonResponse({
                'message': "Registration faild",
                'data': user,
                'isSuccess': False
            })


@api_view(['POST', ])
def executiveRegistration(request):
    if request.method == 'POST':
        print('call')
        if request.data.get("refer_code") is None:
            request.data["refer_code"] = ""
        print('request.data', request.data)
        user = createUser(ExecutiveRegistrationSerializer(data=request.data))
        print('user', user)
        if user == True:
            return JsonResponse({
                'message': "Register successfully",
                'data': 1,
                'isSuccess': True
            }, status=201)
        else:
            return JsonResponse({
                'message': "Registration faild",
                'data': user,
                'isSuccess': False
            })


@api_view(['POST', ])
def customerRegistration(request):
    if request.method == 'POST':
        print('call')
        if request.data.get("refer_code") is None:
            request.data["refer_code"] = ""
        print('request.data', request.data)
        user = createUser(CustomerRegistrationSerializer(data=request.data))
        print('user', user)
        if user == True:
            return JsonResponse({
                'message': "Register successfully",
                'data': 1,
                'isSuccess': True
            }, status=201)
        else:
            return JsonResponse({
                'message': "Registration faild",
                'data': user,
                'isSuccess': False
            })


@api_view(['POST', ])
def sms(request):
    if request.method == 'POST':
        try:
            data = request.data
            phone = data["phone"]
            number = phone.replace("+91", "")
            user = User.objects.filter(phone_no=str(number))
            if not user.exists():
                otp = generateOTP()
                account_sid = TWILIO_ACCOUNT_SID
                auth_token = TWILIO_AUTH_TOKEN
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                    messaging_service_sid='MG4f7fcbc716b63e562c7ddb3282dd2c69',
                    from_='+19498284050',
                    to=phone,
                    body="Dear User,\n"+otp + \
                    " is your one time password (OTP). Please enter the OTP to proceed.\nThank you,\nTeam EventoPackage"
                )
                OtpLog.objects.create(mobile=phone, otp=otp)

                return JsonResponse(
                    {'message': "OTP is sended via SMS",
                     'data': {'phone': phone, 'OTP': otp},
                     'isSuccess': True
                     }, status=201)
            else:
                return JsonResponse(
                    {'message': "Please enter valide phone number",
                     'data': 0,
                     'isSuccess': False
                     }, status=201)
        except Exception as e:
            print('e', e)
            # return JsonResponse(
            #     {'message': "Something went wrong.",
            #      'data': 0, 'isSuccess': False }, status=201)


@api_view(['POST', ])
def verifyOtp(request):
    if request.method == "POST":
        otp = request.data["otp"]

        if otp:
            otp_log = OtpLog.objects.filter(otp=str(otp))
            if otp_log.exists():
                otp_log = otp_log[0]
                otp_log.is_verify = True
                otp_log.save()
                return JsonResponse({"status": True, })
            else:
                return JsonResponse({"status": False, })
        else:
            return JsonResponse(
                {
                    "status": False,
                    'detail': "Invalid mobile otp"
                }
            )


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            fetchUserType = User.objects.filter(email=user)
            serialize = RegistrationSerializer(fetchUserType, many=True)
            # check user type and provide secure code
            # 0 - u0sdja45asdjfhjhads455
            # 1 - u1rewuo456ewerw78rewee
            # 2 - u26fsdfsdtr45dfsdtrvcx
            # 3 - u3osd54sa6dskkhs45sasd
            # 4 - u4osd54sa6dskkhs45sssd
            # 5 - u5osd54sa6dskkhs45aaad
            for data in serialize.data:
                if data["user_type"] == 0:
                    utc = "u0sdja45asdjfhjhads455"
                elif data["user_type"] == 1:
                    utc = "u1rewuo456ewerw78rewee"
                elif data["user_type"] == 2:
                    utc = "u26fsdfsdtr45dfsdtrvcx"
                elif data["user_type"] == 3:
                    utc = "u3osd54sa6dskkhs45sasd"
                elif data["user_type"] == 4:
                    utc = "u4osd54sa6dskkhs45sssd"
                else:
                    utc = "u5osd54sa6dskkhs45aaad"
            return JsonResponse({
                'message': "Login successfully",
                'data': {'token': token.key, 'userId':  token.user_id, 'userTypeCheck': utc},
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Login faild",
            'data': 0,
            'isSuccess': False
        }, status=200)


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if '@' in username:
            try:
                user = User.objects.get(email=username)
            except User.DoesNotExist:
                return None
        else:
            try:
                user = User.objects.get(phone_no=username)
            except User.DoesNotExist:
                return None

        if user.check_password(password):
            return user

    def get_user(self, user_id):
        try:
            return User.objects.get(userId=user_id)
        except User.DoesNotExist:
            return None


class Logout(APIView):
    def post(self, request, format=None):
        request.user.auth_token.delete()
        return JsonResponse({
            'message': "Logout successfully",
            'data': "1",
            'isSuccess': True
        }, status=200)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ApiusergetList(request):
    user = request.user
    fetch = User.objects.filter(email=user)
    serialize = RegistrationSerializer(fetch, many=True)
    return JsonResponse({
        'message': "Data fetch Successfully",
        'data': serialize.data,
        'isSuccess': True
    }, status=200)


@api_view(['GET', 'DELETE'])
# @allowuser(allowrole=['0', '1', '2'])
@permission_classes([IsAuthenticated])
def userdataApi(request, id=0):
    if request.method == 'GET':
        if id != 0:
            reg = User.objects.filter(userId=id)
        else:
            reg = User.objects.all()
        regs_serializer = RegistrationSerializer(reg, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': regs_serializer.data,
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Error while fetching user",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['DELETE'])
@allowuser(allowrole=['0', '1', '2'])
# @permission_classes([IsAuthenticated])
def userdeleteApi(request, id=0):
    if request.method == 'DELETE':
        ser = User.objects.get(userId=id)
        ser.delete()
        return JsonResponse({
            'message': "Deleted Successfully",
            'data': "1",
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Error while deleting user",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['POST'])
def email_otp(request):
    if request.method == 'POST':
        send = EmailSerializer(data=request.data)
        if send.is_valid():
            account = send.save()
            re_email = account.email
            user_email = User.objects.filter(email=re_email).first()
            otp_us = RegistrationSerializer(user_email)
            a = otp_us.data['userId']
            b = otp_us.data['email']
            if user_email:
                o = generateOTP()
                user_email.otp = o
                user_email.save()
                htmlgen = '<p>Your OTP is </p>' + o
                send_mail('OTP request', o, 'help@eventopackage.com', [
                    user_email], fail_silently=False, html_message=htmlgen)
                return JsonResponse({
                    'message': "OTP is send to you'r email id",
                    'data': {
                        'userId': a,
                        'email': b,
                        'otp': o
                    },
                    'isSuccess': True
                }, status=200)
            return JsonResponse({
                'message': "Please enter valid email id!!",
                'data': send.errors,
                'isSuccess': False
            }, status=200)
        else:
            return JsonResponse({
                'message': "Please enter valid email id!!",
                'data': send.errors,
                'isSuccess': False
            }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['PUT'])
def resetpassApi(request):
    if request.method == 'PUT':
        pass_data = JSONParser().parse(request)
        password = User.objects.get(userId=pass_data['userId'])
        reset_password = ResetpasswordSerializer(password, data=pass_data)
        # print(reset_password)
        if reset_password.is_valid():
            reset_password.save()
            return JsonResponse({
                'message': "Password is changed Successfully",
                'data': pass_data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Error while changing password ",
            'data': reset_password.errors,
            'isSuccess': False
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
                'isSuccess': False
    }, status=400)


@api_view(['PUT'])
def forgotpassApi(request):
    if request.method == 'PUT':
        pass_data = JSONParser().parse(request)
        # print("--->",pass_data['email'])
        password = User.objects.get(email=pass_data['email'])
        reset_password = forgotpasswordSerializer(password, data=pass_data)
        # print("--->", reset_password)

        # print(reset_password)
        if reset_password.is_valid():
            reset_password.save()
            return JsonResponse({
                'message': "Password is changed Successfully",
                'data': pass_data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Error while changing password ",
            'data': reset_password.errors,
            'isSuccess': False
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
                'isSuccess': False
    }, status=400)


@api_view(['PUT'])
def updateuser(request):
    if request.method == 'PUT':
        user = request.user.userId
        # name = request.data["name"]
        getuser = User.objects.filter(userId=user)
        serializer = RegistrationSerializer(getuser, many=True)
        print(serializer.data)

        # if name:
        #     User.objects.filter(userId=user).update(name=str(name))
        # if request.data["email"]:
        #     User.objects.filter(userId=user).update(
        #         email=str(request.data["email"]))
        # if request.data["phone_no"]:
        #     User.objects.filter(userId=user).update(
        #         phone_no=str(request.data["phone_no"]))
        # if request.data["profile_img"]:
        #     m = User.objects.get(userId=user)
        #     m.profile_img = request.FILES["profile_img"]
        #     m.save()
        return JsonResponse({
            'message': "Your profile is updated Successfully",
            'data': serializer.data,
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "There is some issue in update",
        'data': 0,
        'isSuccess': True
    }, status=200)


@api_view(['PUT'])
@allowuser(allowrole=['0', '1', '2', '3'])
def updateAnyUser(request):
    if request.method == 'PUT':
        user_id = int(request.data["user_id"])
        name = request.data["name"]
        if User.objects.filter(userId=user_id):
            if name:
                User.objects.filter(userId=user_id).update(name=str(name))
            if request.data["email"]:
                if User.objects.filter(email=str(request.data["email"])):
                    return JsonResponse({
                        'message': "Duplicate email address",
                        'data': 0,
                        'isSuccess': False
                    }, status=404)
                # else :
            if request.data["phone_no"]:
                if User.objects.filter(phone_no=str(request.data["phone_no"])):
                    return JsonResponse({
                        'message': "Duplicate phone number",
                        'data': 0,
                        'isSuccess': False
                    }, status=404)
                else:
                    User.objects.filter(userId=user_id).update(
                        email=str(request.data["email"]))
                    User.objects.filter(userId=user_id).update(
                        phone_no=str(request.data["phone_no"]))
            if request.data["profile_img"]:
                m = User.objects.get(userId=user_id)
                m.profile_img = request.FILES["profile_img"]
                m.save()
            return JsonResponse({
                'message': "Profile is updated Successfully",
                'data': 1,
                'isSuccess': True
            }, status=200)
        else:
            return JsonResponse({
                'message': "User not found!!",
                'data': 0,
                'isSuccess': False
            }, status=404)
    return JsonResponse({
        'message': "There is some issue in update",
        'data': 0,
        'isSuccess': False
    }, status=200)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def wishlistApi(request, id=0):
    if request.method == 'GET':
        user = request.user
        wishlist = Wishlists.objects.filter(user=user)
        wishlists_serializer = WishlistSerializer(wishlist, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': wishlists_serializer.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'POST':
        wishlists_serializer = WishlistSerializer(data=request.data)
        if wishlists_serializer.is_valid():

            wish = wishlists_serializer.data
            userId = wish['user']
            eId = wish['eventId']
            perId = wish['partnerId']
            pId = wish['personalId']

            if eId != None:
                wishlist = Wishlists.objects.filter(user=userId, eventId=eId)
                if wishlist:
                    # print("True")
                    return JsonResponse({
                        'message': "Item is already in wishlist",
                        'data': 1,
                        'isSuccess': True
                    }, status=200)
                else:
                    wishlists_serializer = WishlistSerializer(
                        data=request.data)
                    if wishlists_serializer.is_valid():
                        wishlists_serializer.save()

            elif perId != None:
                wishlist = Wishlists.objects.filter(
                    user=userId, partnerId=perId)
                if wishlist:
                    # print("True")
                    return JsonResponse({
                        'message': "Item is already in wishlist",
                        'data': 1,
                        'isSuccess': True
                    }, status=200)
                else:
                    wishlists_serializer = WishlistSerializer(
                        data=request.data)
                    if wishlists_serializer.is_valid():
                        wishlists_serializer.save()

            elif pId != None:
                wishlist = Wishlists.objects.filter(
                    user=userId, personalId=pId)
                if wishlist:
                    # print("True")
                    return JsonResponse({
                        'message': "Item is already in wishlist",
                        'data': 1,
                        'isSuccess': True
                    }, status=200)
                else:
                    wishlists_serializer = WishlistSerializer(
                        data=request.data)
                    if wishlists_serializer.is_valid():
                        wishlists_serializer.save()

            else:
                wishlists_serializer = WishlistSerializer(data=request.data)
                if wishlists_serializer.is_valid():
                    wishlists_serializer.save()
                    # print("False")
                    return JsonResponse({
                        'message': "Item added in wishlist",
                        'data': wishlists_serializer.data,
                        'isSuccess': True
                    }, status=200)

            return JsonResponse({
                'message': "Item added in wishlist",
                'data': wishlists_serializer.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Insertion Faild",
            'data': wishlists_serializer.errors,
            'isSuccess': False
        }, status=200)
    elif request.method == 'PUT':
        wishlist_data = JSONParser().parse(request)
        wishlist = Wishlists.objects.get(wishId=wishlist_data['wishId'])
        wishlists_serializer = WishlistSerializer(wishlist, data=wishlist_data)
        if wishlists_serializer.is_valid():
            wishlists_serializer.save()
            return JsonResponse({
                'message': "Updeted Successfully",
                'data': wishlist_data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Error while updating wishlist",
            'data': wishlists_serializer.errors,
            'isSuccess': False
        }, status=200)
    elif request.method == 'DELETE':
        wishlist = Wishlists.objects.get(wishId=id)

        wishlist.delete()
        return JsonResponse({
            'message': "Deleted Successfully",
            'data': "1",
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['GET'])
@allowuser(allowrole=['0', '1', '2', '3'])
def allTransactionApi(request):
    if request.method == 'GET':
        transaction = Transactions.objects.all()
        transaction_serializer = TransactionsSerializer(transaction, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': transaction_serializer.data,
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def TransactionApi(request, id=0):
    if request.method == 'GET':
        user = request.user
        transaction = Transactions.objects.filter(user=user)
        transaction_serializer = TransactionsSerializer(transaction, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': transaction_serializer.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'POST':
        transaction_serializer = TransactionsSerializer(data=request.data)
        if transaction_serializer.is_valid():
            transaction_serializer.save()
            return JsonResponse({
                'message': "Inserted Successfully",
                'data': transaction_serializer.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Insertion Faild",
            'data': transaction_serializer.errors,
            'isSuccess': False
        }, status=200)
    elif request.method == 'PUT':
        return JsonResponse({
            'message': "There is no PUT method",
            'data': 0,
            'isSuccess': False
        }, status=200)
    elif request.method == 'DELETE':
        transaction = Transactions.objects.get(id=id)
        transaction.delete()
        return JsonResponse({
            'message': "Deleted Successfully",
            'data': "1",
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def RedeemCoinsApi(request, id=0):
    if request.method == "GET":
        user = request.user
        redeem = RedeemCoins.objects.filter(user=user)
        redeemSerializer = RedeemCoinsSerializer(redeem, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': redeemSerializer.data,
            'isSuccess': True
        }, status=200)
    elif request.method == "POST":
        redeemdata = JSONParser().parse(request)
        redeemSerializers = RedeemCoinsSerializer(data=redeemdata)
        if redeemSerializers.is_valid():
            redeemSerializers.save()
            redeemData = redeemSerializers.data
            redeemAmount = redeemData['Amount']
            redeemUser = redeemData['user']

            user = User.objects.filter(userId=redeemUser)
            user_serializer = RegistrationSerializer(user, many=True)
            coindata = user_serializer.data
            for i in coindata:
                coins = i['coins']
                name = i['name']

                if int(redeemAmount) <= int(coins):
                    user = User.objects.filter(userId=redeemUser).first()
                    user.coins = int(coins) - int(redeemAmount)
                    user.save()

                    remaining = int(coins) - int(redeemAmount)
                    value = {
                        "user": redeemUser,
                        "img": "http://eventopackage.com/static/media/Redeem.png",
                        "translation_type": "Coin Redeem",
                        "details": name,
                        "Amount": remaining
                    }
                    transaction_serializer = TransactionsSerializer(data=value)
                    if transaction_serializer.is_valid():
                        transaction_serializer.save()

                else:
                    return JsonResponse({
                        'message': "You don't have sufficient balance",
                        'data': redeemAmount,
                        'isSuccess': True
                    }, status=200)

            return JsonResponse({
                'message': "Inserted Successfully",
                'data': redeemSerializers.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Insertion Faild",
            'data': redeemSerializers.errors,
            'isSuccess': False
        }, status=200)
    elif request.method == "PUT":
        return JsonResponse({
            'message': "There is no PUT method",
            'data': 0,
            'isSuccess': False
        }, status=200)
    elif request.method == "DELETE":
        return JsonResponse({
            'message': "There is no DELETE method",
            'data': 0,
            'isSuccess': False
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def checkoutApi(request, id=0):
    if request.method == 'GET':
        chko = Checkouts.objects.all()
        chkos_serializer = CheckoutSerializer(chko, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': chkos_serializer.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'POST':
        chko_data = JSONParser().parse(request)
        chkos_serializer = CheckoutSerializer(data=chko_data)
        if chkos_serializer.is_valid():
            chkos_serializer.save()
            return JsonResponse({
                'message': "Inserted Successfully",
                'data': chko_data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Insertion Faild",
            'data': chkos_serializer.errors,
            'isSuccess': False
        }, status=200)
    elif request.method == 'PUT':
        chko_data = JSONParser().parse(request)
        chko = Checkouts.objects.get(chkoId=chko_data['chkoId'])
        chkos_serializer = CheckoutSerializer(chko, data=chko_data)
        if chkos_serializer.is_valid():
            chkos_serializer.save()
            return JsonResponse({
                'message': "Updeted Successfully",
                'data': chko_data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Error while updating Checkout",
            'data': chkos_serializer.errors,
            'isSuccess': False
        }, status=200)
    elif request.method == 'DELETE':
        chko = Checkouts.objects.get(chkoId=id)
        chko.delete()
        return JsonResponse({
            'message': "Deleted Successfully",
            'data': "1",
                    'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def ticketApi(request, id=0):
    if request.method == 'GET':
        user = request.user
        ticket = Tickets.objects.filter(user=user)
        tickets_serializer = TicketSerializer(ticket, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': tickets_serializer.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'POST':
        # ticket_data = JSONParser().parse(request)
        tickets_serializer = TicketSerializer(data=request.data)
        if tickets_serializer.is_valid():
            tickets_serializer.save()
            roomname = 'festumroom'
            data = tickets_serializer.data

            uid = data["user"]
            eid = data["eventId"]
            pid = data["partnerId"]
            psid = data["personalSkillId"]
            tid = data["ticketId"]

            user = User.objects.filter(userId=uid).first()
            if eid != None:
                event = createEvent.objects.filter(eventId=eid).first()
                events_serializer = createEventSerializers(event)
                edata = events_serializer.data
                evd = edata["event"]
                for e in evd:
                    adr = e["address"]
                evd = edata["image"]
                for ev in evd:
                    image = "http://eventopackage.com"+ev["image"]
                    break

                tickets = Tickets.objects.filter(ticketId=tid)
                for ticket in tickets:
                    ticket.holdername = user.name
                    ticket.orgId = edata["User"]
                    ticket.holdercontact = user.phone_no
                    ticket.img = image
                    ticket.amount = edata["price"]
                    ticket.name = edata["display_name"]
                    ticket.address = adr
                    ticket.category = edata["category"]
                    ticket.roomname = roomname
                    ticket.receiver = edata["User"]
                    ticket.save()

            elif pid != None:
                pcom = O_PartnerCompanys.objects.filter(parcomId=pid).first()
                pcom_serializers = O_PartnercompanySerializers(pcom)
                pdata = pcom_serializers.data
                for pic in pdata['photo']:
                    image = "http://eventopackage.com"+pic['photo_file']
                    break

                tickets = Tickets.objects.filter(ticketId=tid)
                for ticket in tickets:
                    ticket.holdername = user.name
                    ticket.holdercontact = user.phone_no
                    ticket.img = image
                    ticket.amount = pdata["price"]
                    ticket.name = pdata["name"]
                    ticket.address = pdata["com_address"]
                    ticket.category = pdata["category"]
                    ticket.roomname = roomname
                    ticket.receiver = pdata["User"]
                    ticket.save()

            elif psid != None:
                prskill = O_PersonalSkills.objects.filter(
                    perskillId=psid).first()
                prskill_serializers = O_PersonalskillSerializers(prskill)
                psdata = prskill_serializers.data
                for pspic in psdata['Photo']:
                    image = "http://eventopackage.com"+pspic['photo_file']
                    break

                tickets = Tickets.objects.filter(ticketId=tid)
                for ticket in tickets:
                    ticket.holdername = user.name
                    ticket.holdercontact = user.phone_no
                    ticket.img = image
                    ticket.amount = psdata['price']
                    ticket.name = psdata['name']
                    ticket.address = psdata['com_address']
                    ticket.category = psdata['pro_category']
                    ticket.roomname = roomname
                    ticket.receiver = psdata['User']
                    ticket.save()

            return JsonResponse({
                'message': "Inserted Successfully",
                'data': tickets_serializer.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Insertion Faild",
            'data': tickets_serializer.errors,
            'isSuccess': False
        }, status=200)
    elif request.method == 'PUT':
        ticket_data = JSONParser().parse(request)
        ticket = Tickets.objects.get(ticketId=ticket_data['ticketId'])
        tickets_serializer = TicketSerializer(ticket, data=ticket_data)
        if tickets_serializer.is_valid():
            tickets_serializer.save()
            return JsonResponse({
                'message': "Updeted Successfully",
                'data': ticket_data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Error while updating of ticket",
            'data': tickets_serializer.errors,
            'isSuccess': False
        }, status=200)
    elif request.method == 'DELETE':
        ticket = Tickets.objects.get(ticketId=id)
        ticket.delete()
        return JsonResponse({
            'message': "Deleted Successfully",
            'data': "1",
                    'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['GET'])
@allowuser(allowrole=['0', '1', '2', '3'])
def allticket(request):
    if request.method == 'GET':
        ticket = Tickets.objects.all()
        tickets_serializer = TicketSerializer(ticket, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': tickets_serializer.data,
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def clients(request):
    if request.method == 'GET':
        user = request.user.userId
        ticket = Tickets.objects.filter(orgId=user)
        tickets_serializer = TicketSerializer(ticket, many=True)
        holder = tickets_serializer.data
        a = []
        for h in holder:
            user = User.objects.filter(userId=h["user"])
            regs_serializer = RegistrationSerializer(user, many=True)
            a.append(regs_serializer.data)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': a,
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Data fetch Successfully",
        'data': 0,
        'isSuccess': False
    }, status=200)


# chat/views.py

def room(request):
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps("festumroom")),
        'userid': mark_safe(json.dumps("2")),
        'receiver': mark_safe(json.dumps("1")),
    })


def privacy(request):
    return render(request, 'privacy_policy.html')


@api_view(['POST', 'GET', ])
@permission_classes([IsAuthenticated])
def chatbot(request):
    if request.method == 'GET':
        user = request.user
        data = ChatBot.objects.filter(
            sender=user).order_by('-timestamp').all()[:5]
        data_serializers = ChatBotSerializers(data, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': data_serializers.data,
            'isSuccess': True
        }, status=200)

    elif request.method == 'POST':
        user = request.user
        msg = JSONParser().parse(request)
        response = bot.get_response(msg['msg'])
        chatresponse = str(response)
        value = {
            'sender': user.userId,
            'message': msg['msg'],
            'reply': chatresponse
        }
        bot_serializer = ChatBotSerializers(data=value)
        if bot_serializer.is_valid():
            bot_serializer.save()

        return JsonResponse({
            'message': "Successfully connected",
            'data': chatresponse,
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Something went wrong",
        'data': 0,
        'isSuccess': False
    }, status=400)


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def AppToken(request, id=0):
    if request.method == "GET":
        data = fcmtoken.objects.all()
        data_serializers = fcmtokenSerializers(data, many=True)
        return JsonResponse({
            'message': "fetched Successfully",
            'data': data_serializers.data,
            'isSuccess': True
        }, status=200)

    elif request.method == "POST":
        user = request.user
        fcm_data = JSONParser().parse(request)
        data = {
            "user": user.userId,
            "apptoken": fcm_data["apptoken"],
            "platform_type": fcm_data["platform_type"]
        }
        getData = fcmtoken.objects.filter(user=user.userId).first()
        if getData:
            fcm_serializer = fcmtokenSerializers(getData, data=data)
            if fcm_serializer.is_valid():
                fcm_serializer.save()
            return JsonResponse({
                'message': "Inserted Successfully",
                'data': fcm_serializer.data,
                'isSuccess': True
            }, status=200)

        else:
            fcm_serializer = fcmtokenSerializers(data=data)
            if fcm_serializer.is_valid():
                fcm_serializer.save()
            return JsonResponse({
                'message': "Inserted Successfully",
                'data': fcm_serializer.data,
                'isSuccess': True
            }, status=200)

    elif request.method == "PUT":
        fcm_data = JSONParser().parse(request)
        fcm = fcmtoken.objects.get(tokId=fcm_data['tokId'])
        fcm_serializer = fcmtokenSerializers(fcm, data=fcm_data)
        if fcm_serializer.is_valid():
            fcm_serializer.save()
            return JsonResponse({
                'message': "Updeted Successfully",
                'data': fcm_serializer.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Error while updating",
            'data': fcm_serializer.errors,
            'isSuccess': False
        }, status=200)

    elif request.method == "DELETE":
        fcm = fcmtoken.objects.get(user=id)
        fcm.delete()
        return JsonResponse({
            'message': "Deleted Successfully",
            'data': "1",
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


# Notifications

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def NotificationDATA(request, id=0):
    if request.method == "GET":
        notificationdata = NotificationData.objects.all()
        notification_serializers = NotificationDataSerializers(
            notificationdata, many=True)
        return JsonResponse({
            'message': "fetched Successfully",
            'data': notification_serializers.data,
            'isSuccess': True
        }, status=200)

    elif request.method == "POST":
        notif_serializers = NotificationDataSerializers(data=request.data)
        if notif_serializers.is_valid():
            notif_serializers.save()
            return JsonResponse({
                "message": "Successfullu inserted",
                "data": notif_serializers.data,
                "isSuccess": True
            }, status=200)
        return JsonResponse({
            "message": "Can not insert the data",
            "data": notif_serializers.errors,
            "isSuccess": True
        }, status=200)

    elif request.method == "PUT":
        notification = NotificationData.objects.filter(id=id).first()
        notification_serializers = NotificationDataSerializers(
            notification, data=request.data)
        if notification_serializers.is_valid():
            notification_serializers.save()
            return JsonResponse({
                'message': "Updeted Successfully",
                'data': notification_serializers.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Error while updating",
            'data': notification_serializers.errors,
            'isSuccess': True
        }, status=200)

    elif request.method == "DELETE":
        notifications = NotificationData.objects.get(id=id)
        notifications.delete()
        return JsonResponse({
            'message': "Deleted Successfully",
            'data': "1",
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def Notifications(request, id=0):
    if request.method == 'GET':
        notification = Notification.objects.all()
        notification_serializers = NotificationSerializers(
            notification, many=True)
        return JsonResponse({
            'message': "fetched Successfully",
            'data': notification_serializers.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'POST':
        notif_serializers = NotificationSerializers(data=request.data)
        if notif_serializers.is_valid():
            notif_serializers.save()
            return JsonResponse({
                "message": "Successfullu inserted",
                "data": notif_serializers.data,
                "isSuccess": True
            }, status=200)
        return JsonResponse({
            "message": "Can not insert the data ....",
            "data": notif_serializers.errors,
            "isSuccess": True
        }, status=200)

    elif request.method == 'PUT':
        notification = Notification.objects.filter(id=id).first()
        notification_serializers = NotificationSerializers(
            notification, data=request.data)
        if notification_serializers.is_valid():
            notification_serializers.save()
            return JsonResponse({
                'message': "Updeted Successfully",
                'data': notification_serializers.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Error while updating",
            'data': notification_serializers.errors,
            'isSuccess': True
        }, status=200)

    elif request.method == 'DELETE':
        notifications = Notification.objects.get(id=id)
        notifications.delete()
        return JsonResponse({
            'message': "Deleted Successfully",
            'data': "1",
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


mycursor = connection.cursor()


@api_view(['POST', ])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def pushnotification(request):
    if request.method == 'POST':
        sms = request.GET.get('sms', "")
        notify = request.GET.get('notify', "")
        email = request.GET.get('email', "")

        if sms == str(1):
            sql = 'SELECT phone_no FROM userapi_user AS u JOIN userapi_notification AS n ON n.user_id = u.userId WHERE n.user_id = u.userId'
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            for x in myresult:
                phone = "+91" + \
                    str(x).replace(',', '').replace(
                        '(', '').replace(')', '').replace('\'', '')
                message = "This is my first sms!!"
                account_sid = TWILIO_ACCOUNT_SID
                auth_token = TWILIO_AUTH_TOKEN
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                    from_='+19085290875',
                    to=phone,
                    body=message
                )

        if email == str(1):
            sql = 'SELECT email FROM userapi_user AS u JOIN userapi_notification AS n ON n.user_id = u.userId WHERE n.user_id = u.userId'
            mycursor.execute(sql)
            mails = mycursor.fetchall()
            for m in mails:
                mail = str(m).replace(',', '').replace(
                    '(', '').replace(')', '').replace('\'', '')
                user_email = mail
                email_message = "This is the TEST mail from Rutvik!!"
                htmlgen = '<p> It seems you have new notification </p>' + email_message
                send_mail('New Updates', email_message, 'help@eventopackage.com', [
                    user_email], fail_silently=False, html_message=htmlgen)

        if notify == str(1):
            data = request.data
            sql = 'SELECT apptoken FROM userapi_fcmtoken where user_id in (' + \
                data['users'] + ');'
            mycursor.execute(sql)
            tokens = mycursor.fetchall()
            for t in tokens:
                tokenin = str(t).replace(',', '').replace(
                    '(', '').replace(')', '').replace('\'', '')
                tokens = [tokenin]
                fcm.sendPush("Evento Package", "test notification", tokens)

        return JsonResponse({
            'message': "Successfully Sended",
            'data': 1,
            'isSuccess': True
        })
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def subscriptionplan(request, id=0):
    if request.method == "GET":
        if id != 0:
            subscription = Subscriptionplan.objects.filter(id=id)
        else:
            subscription = Subscriptionplan.objects.all()
        subscription_data = SubscriptionplanSerializers(
            subscription, many=True)
        return JsonResponse({
            'message': "Successfully fatched",
            'data': subscription_data.data,
            'isSuccess': True
        })
    elif request.method == "POST":
        subscription = JSONParser().parse(request)
        subscription = SubscriptionplanSerializers(data=subscription)
        if subscription.is_valid():
            subscription.save()
            return JsonResponse({
                "message": "Successfully saved",
                "data": subscription.data,
                "isSuccess": True
            })
        return JsonResponse({
            'message': "Insertiong Faild",
            'data': subscription.errors,
            'isSuccess': False
        }, status=200)

    elif request.method == "PUT":
        subscription_data = JSONParser().parse(request)
        subscription = Subscriptionplan.objects.get(
            id=subscription_data['id'])
        subscription_serializer = SubscriptionplanSerializers(
            subscription, data=subscription_data)
        if subscription_serializer.is_valid():
            subscription_serializer.save()
            return JsonResponse({
                'message': "Updeted Successfully",
                'data': subscription_serializer.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Error while updating",
            'data': subscription_serializer.errors,
            'isSuccess': False
        }, status=200)

    elif request.method == "DELETE":
        subscription = Subscriptionplan.objects.get(id=id)
        subscription.delete()
        return JsonResponse({
            'message': "Deleted Successfully",
            'data': "1",
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


client = razorpay.Client(
    auth=("rzp_test_ONkjQqwBphi9zw", "skWhL26zyG3gOcbFqFzZXYhq"))


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def OrderIdGenerate(request, id=0):
    if request.method == 'POST':
        userid = request.user.userId
        orderId = JSONParser().parse(request)
        total_amount = orderId["total_amount"]
        currency = orderId["currency"]
        data = {"amount": total_amount, "currency": currency,
                "receipt": "order_rcptid_"+str(userid)}
        payment = client.order.create(data=data)
        return JsonResponse({
            'message': "OrderId",
            'data': payment,
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def UserMembership(request, id=0):
    if request.method == 'GET':
        member = Membership.objects.all()
        member_data = MembershipSerializers(member, many=True)
        list_data = member_data.data
        for list in list_data:
            if list['date_of_expiry'] == str(datetime.datetime.now().date()):
                membership = Membership.objects.get(id=list['id'])
                membership.status = 2
                membership.save()

        member = Membership.objects.all()
        member_data = MembershipSerializers(member, many=True)
        return JsonResponse({
            'message': "Successfully fatched",
            'data': member_data.data,
            'isSuccess': True
        })

    elif request.method == 'POST':
        user = request.user.userId
        members = JSONParser().parse(request)
        planid = members["planid"]
        total_price = members["total_price"]
        ordId = members["order_id"]

        member = Membership.objects.filter(user=user).last()
        member_data = MembershipSerializers(member)
        mdata = member_data.data
        if mdata:
            if mdata["status"] == "1":
                return JsonResponse({
                    "message": "You already have Subscription plan running",
                    "data": 1,
                    "isSuccess": True
                })

            else:
                subscription = Subscriptionplan.objects.filter(id=planid)
                subscription_data = SubscriptionplanSerializers(
                    subscription, many=True)
                datas = subscription_data.data

                # if plantype == "Monthly":
                for data in datas:
                    member = {
                        "user": user,
                        "plan_name": data["plan_name"],
                        "total_price": total_price,
                        "video_count": data["video_count"],
                        "image_count": data["image_count"],
                        "sms": data["sms"],
                        "notifications": data["notifications"],
                        "emails": data["emails"],
                        "socialmedia_promotion": data["socialmedia_promotion"],
                        "date_of_expiry": datetime.datetime.now().date() + datetime.timedelta(days=30),
                        "status": 1,
                        "order_id": ordId
                    }
                    membership = MembershipSerializers(data=member)
                    if membership.is_valid():
                        membership.save()
                        return JsonResponse({
                            "message": "Successfully saved",
                            "data": membership.data,
                            "isSuccess": True
                        })

                # elif plantype == "Yearly":
                #     for data in datas:
                #         member = {
                #             "user": user,
                #             "plan_name": data["plan_name"],
                #             "total_price": total_price,
                #             "yearly_price": data["yearly_price"],
                #             "discount_value": data["discount_value"],
                #             "discount_type": data["discount_type"],
                #             "video_count": data["video_count"],
                #             "image_count": data["image_count"],
                #             "sms": data["sms"],
                #             "notifications": data["notifications"],
                #             "emails": data["emails"],
                #             "socialmedia_promotion": data["socialmedia_promotion"],
                #             "date_of_expiry": datetime.datetime.now().date() + datetime.timedelta(days=365),
                #             "status": 1,
                #             "order_id" : payment["id"]
                #         }
                #         membership = MembershipSerializers(data=member)
                #         if membership.is_valid():
                #             membership.save()
                #             return JsonResponse({
                #                 "message": "Successfully saved",
                #                 "data": membership.data,
                #                 "isSuccess": True
                #             })

                return JsonResponse({
                    'message': "Insertiong Faild",
                    'data': 0,
                    'isSuccess': True
                }, status=200)
        return JsonResponse({
            'message': "Something is wring",
            'data': 0,
            'isSuccess': True
        }, status=200)

    elif request.method == 'PUT':
        member = JSONParser().parse(request)
        membership = Membership.objects.filter(user=id)
        member_serializer = MembershipSerializers(member, data=membership)
        if member_serializer.is_valid():
            member_serializer.save()
            return JsonResponse({
                'message': "Updeted Successfully",
                'data': member_serializer.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Error while updating",
            'data': member_serializer.errors,
            'isSuccess': True
        }, status=200)

    elif request.method == 'DELETE':
        membership = Membership.objects.get(id=id)
        membership.delete()
        return JsonResponse({
            'message': "Deleted Successfully",
            'data': "1",
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def advertisementapi(request, id=0):
    if request.method == "GET":
        advertis = Advertisement.objects.all()
        advertis_serializers = AdvertisementSerializers(advertis, many=True)
        return JsonResponse({
            "message": "Successfully fatched",
            "data": advertis_serializers.data,
            "isSuccess": True,
        }, status=200)

    elif request.method == "POST":
        advertis_serializers = AdvertisementSerializers(data=request.data)
        if advertis_serializers.is_valid():
            advertis_serializers.save()
            return JsonResponse({
                "message": "Successfullu inserted",
                "data": advertis_serializers.data,
                "isSuccess": True
            }, status=200)
        return JsonResponse({
            "message": "Can not insert the data",
            "data": advertis_serializers.errors,
            "isSuccess": True
        }, status=200)

    elif request.method == "PUT":
        advertis = Advertisement.objects.filter(id=id).first()
        advertis_serializers = AdvertisementSerializers(
            advertis, data=request.data)
        if advertis_serializers.is_valid():
            advertis_serializers.save()
            return JsonResponse({
                'message': "Updeted Successfully",
                'data': advertis_serializers.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Error while updating",
            'data': advertis_serializers.errors,
            'isSuccess': True
        }, status=200)

    elif request.method == "DELETE":
        advertis = Advertisement.objects.get(id=id)
        advertis.delete()
        return JsonResponse({
            'message': "Deleted Successfully",
            'data': "1",
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


# Create your views here.
@api_view(['POST', 'GET', 'PUT', 'DELETE'])
def GetInTouchApi(request, id=0):
    if request.method == 'GET':
        getin = GetInTouch.objects.all()
        getin_serializer = GetInTouchSerializers(getin, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': getin_serializer.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'POST':
        getin_data = JSONParser().parse(request)
        getin_serializer = GetInTouchSerializers(data=getin_data)
        if getin_serializer.is_valid():
            getin_serializer.save()

            # mail system
            name = getin_serializer.data["name"]
            contact = getin_serializer.data["contact"]
            email = getin_serializer.data["email"]
            message = getin_serializer.data["message"]

            m = message
            htmlgen = '<p>Email</p>' + m + '<p>You have successfully submited your query</p>'
            send_mail('Email request', m, 'help@eventopackage.com', [
                email], fail_silently=False, html_message=htmlgen)

            companyEmail = "devrutvik.scalelot@gmail.com"
            m = message
            e = email
            c = contact
            n = name
            htmlgen = '<p>Name</p>' + n + '<p>Contact</p>' + \
                c + '<p>Email</p>' + e + '<p>Message</p>' + m
            send_mail('Email request', n, 'help@eventopackage.com', [
                companyEmail], fail_silently=False, html_message=htmlgen)

            return JsonResponse({
                'message': "Inserted Successfully",
                'data': getin_data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Insertion Faild",
            'data':  getin_serializer.errors,
            'isSuccess': False
        }, status=200)
    elif request.method == 'PUT':
        getin_data = JSONParser().parse(request)
        getin = GetInTouch.objects.get(gitId=getin_data['gitId'])
        getin_serializer = GetInTouchSerializers(getin, data=getin_data)
        if getin_serializer.is_valid():
            getin_serializer.save()
            return JsonResponse({
                'message': "Updeted Successfully",
                'data': getin_data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Error while updating refers ",
            'data': getin_serializer.errors,
            'isSuccess': False
        }, status=200)
    elif request.method == 'DELETE':
        getin = GetInTouch.objects.get(gitId=id)
        getin.delete()
        return JsonResponse({
            'message': "Deleted Successfully",
            'data': "1",
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def excelusers(request, id=0):
    if request.method == 'GET':
        user = request.user.userId
        # usertype = request.user.user_type
        # print("usertype----->", usertype)
        excel = exceluser.objects.all(organizer=user)
        excel_serializer = excelUserSerializers(excel, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': excel_serializer.data,
            'isSuccess': True
        }, status=200)

    elif request.method == 'POST':
        orgId = request.user.userId
        excel_data = JSONParser().parse(request)
        for e in excel_data:
            value = {
                "orgID": orgId,
                "email": e['email'],
                "mobile_no": e['mobile_no'],
                "name":  e['name']
            }
            excel_serializer = excelUserSerializers(data=value)
            if excel_serializer.is_valid():
                excel_serializer.save()
        return JsonResponse({
            'message': "Inserted Successfully",
            'data': 1,
            'isSuccess': True
        }, status=200)

    elif request.method == 'DELETE':
        excel = exceluser.objects.get(id=id)
        excel.delete()
        return JsonResponse({
            'message': "Deleted Successfully",
            'data': "1",
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)
