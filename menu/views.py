from django.shortcuts import render

def home(request):
    return render(request, 'menu/home.html')

def about(request):
    return render(request, 'menu/about.html')

def team(request):
    return render(request, 'menu/team.html')

def history(request):
    return render(request, 'menu/history.html')

def contact(request):
    return render(request, 'menu/contact.html')
