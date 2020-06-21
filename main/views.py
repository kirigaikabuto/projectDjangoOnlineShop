from django.shortcuts import render,HttpResponse


def main_func(request):
    return render(request,"main/index.html")
