from django.urls import path

from . import views

urlpatterns = [
    path('', views.ChannelList.as_view()),
    path('<slug>/', views.ChannelDetail.as_view()),
    path('<slug:channel>/feed/', views.RSSFeed.as_view()),
    path('<slug:channel>/<slug:item>/', views.ItemDetail.as_view()),
]
