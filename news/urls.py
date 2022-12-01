from django.urls import path
from .views import *

urlpatterns = [
    path('',main),
    path('contact',contact,name='cont'),
    path('category',category,name='cat'),
    path('single',single,name='single'),
    path('sport',sport,name='Sport'),
    # path('single',single,name='single'),
    path('news_d/<int:pk>/',BaseDetailview.as_view(), name='news_d'),
    path('new_top/<int:pk>/',Newtopdetail.as_view(), name='new_top'),
    path('mostnew/<int:pk>/',Mostnewdetail.as_view(), name='mostnew'),
    path('cate_det/<int:pk>/',CategorDetail.as_view(), name='cate_det'),
    
]