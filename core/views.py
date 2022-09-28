from django.shortcuts import render

def getHome(request):
    return render(request, 'index.html')