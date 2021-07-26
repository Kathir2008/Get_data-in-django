from django.shortcuts import render
from getapp.models import data
# Create your views here.
def result(request):
    var = data.objects.all()
    display = {'key' : var}
    return render(request , 'demo.html' ,context=display)