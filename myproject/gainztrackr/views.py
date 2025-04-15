from django.shortcuts import render

def home(request):
    retcode = 200
    context = {}
    return render(request, '', context, status=retcode)