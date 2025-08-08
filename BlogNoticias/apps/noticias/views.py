from django.shortcuts import render

def vista_inicio(request):
    return render(request, 'index.html')
