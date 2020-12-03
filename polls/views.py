from django.shortcuts import render, redirect
from .models import Notice
import logging
from polls.forms import NoticeForm

logger = None


def initLogger():
    global logger
    if logger == None:
        logger = logging.getLogger( "django.db.backends" )
        logger.setLevel( logging.DEBUG )
        logger.addHandler( logging.StreamHandler() )


def index(request):
    initLogger()
    notices = Notice.objects.all()
    # notices = notices.filter(pub_start__lte=timezone.now())
    # notices = notices.filter(pub_end__gte=timezone.now())
    context = {'notices': notices}  # dictionary type
    return render( request, 'polls/index.html', context )


def news(request):
    if request.method == "POST":
        form = NoticeForm(request.POST)
        if form.is_valid():
            new = Notice( notice_title=form.cleaned_data['title'],
                          notice_text=form.cleaned_data['text'],
                          pub_start=form.cleaned_data['start'],
                          pub_end=form.cleaned_data['end'] )
            new.save()
            return redirect( 'polls' )
    context = {'form': NoticeForm()}
    return render( request, 'polls/edit.html', context )


def deletes(request, deleteId=None):
    if deleteId != None:
        delNotice = Notice.objects.get( id=deleteId )
        if delNotice != None:
            delNotice.delete()
    return redirect( 'polls' )
