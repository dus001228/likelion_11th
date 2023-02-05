from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def joinus(request):
    return render(request, 'joinus.html')

def login(request):
    return render(request, 'login.html')

def test(request):
    return render(request, 'test.html')