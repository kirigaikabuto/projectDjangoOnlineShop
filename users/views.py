from django.shortcuts import render,HttpResponse


def login_page(request):
    return HttpResponse("It is login page")


def register_page(request):
    return HttpResponse("it is register.page")