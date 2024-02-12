from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def secondPage(request):
    return render(request, 'rooms.html')
