from django.urls import path
from posts import views

urlpatterns = [
    path( '', views.index, name="posts" ),
    path( 'new', views.new, name='new' ),
    path( 'delete/<int:deleteId>', views.delete, name='delete' ),

    path('notices/',views.notice_list),
    path('notices/<int:id>/',views.notice_detail),
]
