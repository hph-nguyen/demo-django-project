from django.http import HttpResponse

def index(request):
    return HttpResponse("Posts Seite")
# Create your views here.
