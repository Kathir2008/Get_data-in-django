from django.shortcuts import redirect, render
from appdata.models import demo
# Create your views here.
def set(request):
    if request.method == 'POST' :
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')

        DB = demo(
            Mail = email ,
            password = pwd
        )
        DB.save()
        return redirect('bf')
    return render(request , 'design.html')

def get(request):
    get_object = demo.objects.all()
    table = {'keys': get_object}
    return render(request , 'design.html' , context=table)