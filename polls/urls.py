from django.urls import path
from polls import views

urlpatterns = [
    path( '', views.index, name="polls"),
    path( 'news', views.news, name='news' ),
    path( 'delete/<int:deleteId>', views.deletes, name='deletes' ),
]
