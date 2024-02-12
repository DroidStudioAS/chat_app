from django.shortcuts import render
# Create your views here.

rooms = [
    {'id':1, "name": 'lets learn python'},
    {'id': 2, "name": 'lets learn php'},
    {'id': 3, "name": 'lets python'}

]

def home(request):
    return render(request, 'base/home.html', {"rooms":rooms})

def secondPage(request, pk):
    return render(request, 'base/room.html')
