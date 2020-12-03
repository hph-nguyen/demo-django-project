from django.shortcuts import render, redirect
from .forms import NoticeForm
from .models import Notice
from django.utils import timezone
import logging
from django.contrib.auth.decorators import login_required
import time
from django.contrib.admin.views.decorators import staff_member_required

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
    #notices = notices.filter(pub_start__lte=timezone.now())
    #notices = notices.filter(pub_end__gte=timezone.now())
    current = time.strftime(" %H:%M - %d.%m.%y",time.localtime())
    context = {'notices': notices, 'now': current, 'time':time.localtime()}  #dictionary type
    return render ( request, 'posts/index.html', context )

@login_required
def new(request):
    if request.method == "POST":
        form = NoticeForm(request.POST)
        if form.is_valid():
            newNotice = Notice( notice_title=form.cleaned_data['title'],
                                notice_text=form.cleaned_data['text'],
                                pub_start=form.cleaned_data['start'],
                                pub_end=form.cleaned_data['end'])
            newNotice.save()
            return redirect('posts')
    context = {'form' : NoticeForm()}
    return render(request, 'posts/edit.html', context)

@staff_member_required
def delete(request, deleteId=None):
    if deleteId !=None:
        delNotice = Notice.objects.get(id=deleteId)
        if delNotice != None:
            delNotice.delete()
    return redirect('posts')



