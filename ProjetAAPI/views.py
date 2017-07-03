# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .youtubeAPI import youtube_search

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.exceptions import ParseError
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import Drink, Queue, Cocktail, UserInformation, Token
from .serializers import DrinkSerializer, CocktailSerializer, QueueSerializer,UserSerializer, UserInformationSerializer,CocktailSerializerGet
from django.contrib.auth import authenticate
from base64 import b64decode
from .auth import get_or_create_token, get_basic_auth,check_request_token
from django.contrib.auth.hashers import make_password
import uuid

# -------------
# --- LOGIN ---
# -------------

@csrf_exempt
def login(request):
    basic = get_basic_auth(request)

    if basic is not None:
        log = b64decode(bytes(basic, 'ascii')).decode('ascii').split(':')
        user = authenticate(username=log[0], password=log[1])
        print(user)
        if user is not None:
            token = get_or_create_token(user)
            return JsonResponse(data={'token': token.hash})
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

# -------------
# --- DRINK ---
# -------------


@csrf_exempt
def drink_list(request):
    if request.method == 'GET':
        if check_request_token(request):
            drinks = Drink.objects.all()
            serializer = DrinkSerializer(drinks, many=True)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        else:
            return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    elif request.method == 'POST':
        try:
            data = JSONParser().parse(request)
        except ParseError:
            return HttpResponse(status=400)
        serializer = DrinkSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def drink_detail(request, pk):
    try:
        drink = Drink.objects.get(pk=pk)
    except Drink.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        try:
            data = JSONParser().parse(request)
        except ParseError:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        serializer = DrinkSerializer(drink, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        drink.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


# -------------
# --- QUEUE ---
# -------------

@csrf_exempt
def queue_list(request):
    if request.method == 'GET':
        queues = Queue.objects.all()
        serializer = QueueSerializer(queues, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        try:
            data = JSONParser().parse(request)
        except ParseError:
            return HttpResponse(status=400)
        serializer = QueueSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def queue_detail(request, pk):
    try:
        queue = Queue.objects.get(pk=pk)
    except queue.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QueueSerializer(queue)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        try:
            data = JSONParser().parse(request)
        except ParseError:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        serializer = QueueSerializer(queue, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        queue.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
def deleteAllQueue(request):
    queue = Queue.objects.all()
    queue.delete()
    return HttpResponse(status=status.HTTP_200_OK)

# ----------------
# --- COCKTAIL ---
# ----------------


@csrf_exempt
def cocktail_list(request):
    if request.method == 'GET':
        cocktails = Cocktail.objects.all()
        serializer = CocktailSerializerGet(cocktails, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        if check_request_token(request):
            try:
                data = JSONParser().parse(request)
            except ParseError:
                return HttpResponse(status=400)

            serializer = CocktailSerializer(data=data)
            if serializer.is_valid():
                serializer.save()

                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def cocktail_detail(request, pk):
    try:
        cocktail = Cocktail.objects.get(pk=pk)
    except Cocktail.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CocktailSerializerGet(cocktail)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        try:
            data = JSONParser().parse(request)
        except ParseError:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        serializer = CocktailSerializer(cocktail, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cocktail.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


# ----------------
# --- USER ---
# ----------------

@csrf_exempt
def user_list(request):

    if request.method == 'GET':
        user = UserInformation.objects.all()
        serializer = UserInformationSerializer(user, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    elif check_request_token(request):
        if request.method == 'POST':
            try:
                data = JSONParser().parse(request)
            except ParseError:
                return HttpResponse(status=400)
            password = data["user"]["password"]
            passhash = make_password(password)
            data["user"]["password"] = passhash
            print(data["user"]["password"])
            serializer = UserInformationSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
def user_detail(request, pk):
    coins = request.GET.get('addCoin', 0)
    print(coins)
    try:
        user = UserInformation.objects.get(pk=pk)
    except user.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = UserInformationSerializer(user)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        try:
            data = JSONParser().parse(request)
        except ParseError:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        serializer = UserInformationSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def commander(request, pk):
    if check_request_token(request):
        basic = get_basic_auth(request)
        token = Token.objects.get(hash=basic)
        user = token.user
        cocktail = Cocktail.objects.get(pk=pk)
        if cocktail.enoughmoney(user):
            queue = Queue(user=user.userinformation, cocktail=cocktail , uuid=uuid.uuid4())
            queue.save()
            UserInformation.objects.filter(pk=user.userinformation.id).update(coin=(user.userinformation.coin - cocktail.prix))
            data = QueueSerializer(queue)
            return JsonResponse(data=data.data, safe=False, status=status.HTTP_200_OK)
        else:
            return JsonResponse(data=False,safe=False,status=status.HTTP_200_OK)
        return HttpResponse(status=status.HTTP_200_OK)
    else:
        return HttpResponse(status=status.HTTP_501_NOT_IMPLEMENTED)



