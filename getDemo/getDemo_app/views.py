from django.shortcuts import render
from getDemo_app.models import GK
# Create your views here.
def value(request):
    objects = GK.objects.all()
    kathir ={"display" : objects}
    return render(request , "demo.html" , context=kathir)