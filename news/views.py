from django.shortcuts import render
from requests import request
from .models import *
from django.views.generic import *


def base(request):
    d=Position.objects.all()
    new_top=New.objects.all()[0:4]
    context = {
        'positions':d,
        'newtop':new_top,

    }
    return render(request,'index.html', context)
def category(request):
    d=Position.objects.all()
    new_top=New.objects.all()[0:4]
    context = {
        'positions':d,
        'newtop':new_top,
    }


    return render(request,'category.html', context)
def contact(request):
    d=Position.objects.all()
    new_top=New.objects.all()[0:4]
    context = {
        'positions':d,
        'newtop':new_top,
    }
    return render(request,'contact.html', context)
def single(request):
    d=Position.objects.all()
    new_top=New.objects.all()[0:4]
    context = {
        'positions':d,
        'newtop':new_top,
        
    }
    return render(request,'single.html', context)

def main(request):
    a=New.objects.all()
    new_top=New.objects.order_by('-id')[2:5]
    d=Position.objects.all()
    tibbiyot=New.objects.order_by('-id')[0:5]
    mn=New.objects.all()[0:8]
    context = {
        'tibbiyot':tibbiyot,
        'positions':d,
        'newtop':new_top,
        'mostnew':mn,
    }

    # talim=New.objects.filter(position_id =2)
    # uzb=New.objects.filter(position_id =3)
    # xorij=New.objects.filter(position_id =4)
    # sport=New.objects.filter(position_id =5)
    return render(request,'index.html', context)

class BaseDetailview(DetailView):
    model=New
    template_name='detail_news.html'
    context_object_name='det_new'

class Newtopdetail(DetailView):
    model=New
    template_name='detail_news.html'
    context_object_name='det_new'

class Mostnewdetail(DetailView):
    model=New
    template_name='detail_news.html'
    context_object_name='det_new'

def sport(request):
    a=Position.objects.all()
    # new_top=New.objects.all()[0:4]
    d=Position.objects.all()
    context={"pos":a,
    'positions':d,
    }
    # n = New.objects.filter(position_id = 1)
    return render(request, 'content.html', context)


class CategorDetail(DetailView):
    model=New
    template_name='categor_det.html'
    # context_object_name='test'
    # def get_queryset(seltestf, **kwargs):
    #     context = super(CategorDetail, self).get_context_data(**kwargs)
    #     pk = self.kwargs['pk']
    #     kategor = New.objects.filter(position_id=1)
    #     context['categor'] = kategor
    #     return  context
    def get_context_data(self, **kwargs):
        context = super(CategorDetail, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        kategor = New.objects.filter(position_id=pk)
        context['categor'] = kategor
        return context
