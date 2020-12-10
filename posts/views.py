from django.shortcuts import render, redirect
from .forms import NoticeForm
from .models import Notice
import logging
from django.contrib.auth.decorators import login_required
import time
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse, HttpResponse
from .serializers import NoticeSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

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
    current = time.strftime( " %H:%M - %d.%m.%y", time.localtime() )
    context = {'notices': notices, 'now': current, 'time': time.localtime()}  # dictionary type
    return render( request, 'posts/index.html', context )


@login_required
def new(request):
    if request.method == "POST":
        form = NoticeForm( request.POST )
        if form.is_valid():
            newNotice = Notice( notice_title=form.cleaned_data['title'],
                                notice_text=form.cleaned_data['text'],
                                pub_start=form.cleaned_data['start'],
                                pub_end=form.cleaned_data['end'] )
            newNotice.save()
            return redirect( 'posts' )
    context = {'form': NoticeForm()}
    return render( request, 'posts/edit.html', context )


@staff_member_required
def delete(request, deleteId=None):
    if deleteId != None:
        delNotice = Notice.objects.get( id=deleteId )
        if delNotice != None:
            delNotice.delete()
    return redirect( 'posts' )


@csrf_exempt
def notice_list(request):
    if request.method == 'GET':
        notices = Notice.objects.all()
        serializer = NoticeSerializer( notices, many=True )
        return JsonResponse( serializer.data, safe=False )
    elif request.method == 'POST':
        data = JSONParser().parse( request )
        serializer = NoticeSerializer( data=data )
        if serializer.is_valid():
            serializer.save()
            return JsonResponse( serializer.data, status=201 )
        return JsonResponse( serializer.errors, status=400 )


@csrf_exempt
def notice_detail(request, id):
    try:
        notice = Notice.objects.get( id=id )
    except Notice.DoesNotExist:
        return HttpResponse( status=404 )
    if request.method == 'GET':
        serializer = NoticeSerializer( notice )
        return JsonResponse( serializer.data )
    elif request.method == 'PUT':
        data = JSONParser().parse( request )
        serializer = NoticeSerializer( notice, data=data )
        if serializer.is_valid():
            serializer.save()
            return JsonResponse( serializer.data )
        return JsonResponse( serializer.errors, status=400 )
    elif request.method == 'DELETE':
        notice.delete()
        return HttpResponse( status=404 )
