from django.shortcuts import render
from django.http import HttpResponse
from visitors.models import Visitor

def index(request):
    
    all_visitors = Visitor.objects.all()
    context = {
        "page_name": "Dashboard",
        "all_visitors": all_visitors
    }
    return render(request, 'index.html', context)