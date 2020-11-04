from django.http import HttpResponse

def index(request):
    return HttpResponse("Polls Seite")
# Create your views here.
