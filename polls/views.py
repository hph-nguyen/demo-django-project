from django.shortcuts import render, redirect
from .models import Notice
from django.utils import timezone
import logging

logger = None


def initLogger():
    global logger
    if logger == None:
        logger = logging.getLogger("django.db.backends")
        logger.setLevel(logging.DEBUG)
        logger.addHandler(logging.StreamHandler())


def index(request):
    initLogger()
    notices = Notice.objects.all()
    notices = notices.filter(pub_start__lte=timezone.now())
    notices = notices.filter(pub_end__gte=timezone.now())
    context = {'notices': notices}  # dictionary type
    return render(request, 'polls/index.html', context)


#def delete(request, deleteId=None):
 #   if deleteId != None:
  #      delNotice = Notice.objects.get(id=deleteId)
   #     if delNotice != None:
    #        delNotice.delete()
    # return redirect('index')
