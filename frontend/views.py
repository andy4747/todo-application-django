from django.shortcuts import render

# Create your views here.

def list_view(request):
    return render(request,'frontend/index.html')