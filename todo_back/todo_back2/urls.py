from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('list/', views.ListPageView.as_view(), name='list'),
    path('list_new/', views.ListNewPageView.as_view(), name='list_new'),
    path('list_new/<int:pk>', views.PostDetailView.as_view(), name = 'post_detail')
]
