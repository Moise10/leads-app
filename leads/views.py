from django.shortcuts import render
from .models import User, Lead, Agent

# Create your views here.

def home_page(request):
  leads = Lead.objects.all()
  context = {
    "leads": leads
  }
  return render(request, 'second_page.html', context)