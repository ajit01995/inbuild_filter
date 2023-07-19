from django.shortcuts import render

# Create your views here.
def inbuilt_filter(request):
    d={'p':'hello world'}
    return render(request,'inbuilt_filter.html',d)
