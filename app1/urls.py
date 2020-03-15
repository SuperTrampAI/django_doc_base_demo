# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 12:02
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
# __create_data__=2020/3/14 12:02
# @Description: add Description
from django.urls import path

from app1 import views

app_name='app1'
urlpatterns=[
    # ex: /polls/
    #path('', views.index, name='index'),
    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
