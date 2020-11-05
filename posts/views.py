from django.shortcuts import render
import time
def index(request):
    timestring = time.strftime("%H:%M:%S",time.localtime())
    context = {'now': timestring, 'current':time.localtime()}  #dictionary type
    return render (request, 'posts/posts.html',context)

