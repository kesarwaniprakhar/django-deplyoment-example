from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html')

def another_template(request):
    context_dict = {'name': 'this name' , 'number' : 100}
    return render(request, 'basicapp/another.html', context = context_dict)


def third(request):
    return render(request, 'basicapp/three.html')
