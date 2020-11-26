from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="POST"),
    path('new',views.new,name='new'),
]