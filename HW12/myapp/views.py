from django.shortcuts import render
from .models import User

# Create your views here.

def user_name(request):
    users = User.objects.values('name','age')
    return render(request, 'index.html', {'users': users})
