from django.http import HttpResponse

# Create your views here.


def january(request):
    return HttpResponse("Eat only veegtables")


def february(request):
    return HttpResponse("Workup everyday")
