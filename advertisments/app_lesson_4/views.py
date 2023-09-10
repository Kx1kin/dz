from django.shortcuts import render
from django.http import HttpResponse

def dz(request):
    return HttpResponse('Домашка по 4 занятию')
