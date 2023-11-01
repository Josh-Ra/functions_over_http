from django.http.response import HttpResponse
from django.http.request import HttpRequest

import random


def hello_view(request: HttpRequest, name:str) -> str:
    return HttpResponse(f'Hello, {name}!')


def roll_die_view(request: HttpRequest, sides:int) -> int:
    roll = random.randint(1, sides)
    return HttpResponse(roll)


def random_between_view(request:HttpRequest, lo:int, hi:int) -> int:
    return HttpResponse(random.randint(lo, hi))

def add_view(request:HttpRequest, num1:int, num2:int) -> int:
    return HttpResponse(num1 + num2)

def hey_view(request:HttpRequest, name:str) -> str:
    return HttpResponse(f'Hey, {name}!')

def age_in_view(request:HttpRequest, Year:int, BirthYear:int) -> int:
    return HttpResponse(Year - BirthYear)

def order_total_view(request:HttpRequest, burg:int, fry:int, drinks:int) -> int:
    return HttpResponse((burg*4.5)+(fry*1.5)+drinks)

