from django.shortcuts import render
def handler404(request):
    return render(request,'404.html', context={})

def handler500(request):
    return render(request,'500.html', context={})

def base(request):
    return render(request, 'base.html', context={})