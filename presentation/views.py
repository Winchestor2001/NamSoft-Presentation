from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def sort_presentation_detail(presentations):
    result = []
    for presentation in presentations:
        check_presentation = PresentationDetail.objects.filter(presentation=presentation).order_by('pk')
        if check_presentation:
            result.append(
                check_presentation
            )
    
    return result


@login_required(login_url='login')
def home(request):
    subjects = Subject.objects.all()
    context = {'subjects': subjects}
    return render(request, 'presentation/home.html', context)


@login_required
def presentations_page(request, pk):
    presentations = Presentation.objects.filter(subject__pk=pk)
    presentation_details = sort_presentation_detail(presentations)
    context = {'presentations': presentations, 'subject': presentations[0].subject, 'presentation_details': presentation_details}
    return render(request, 'presentation/presentation.html', context)


@login_required
def presentation_detail_page(request):
    presentation_pk = request.GET.get('presentation_pk')
    presentation_detail = PresentationDetail.objects.filter(pk=presentation_pk)
    data = serializers.serialize('json', presentation_detail)
    return HttpResponse(data, content_type="application/json")


def login_page(request):
    context = {}
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        usr = authenticate(username=uname, password=pwd)
        if usr:
            login(request, usr)
            return redirect('/')
        else:
            context['message'] = 'username yoki password xato!!!'
            context['col'] = 'danger'
    return render(request, 'presentation/login_page.html', context)


@login_required
def logout_page(request):
    logout(request)
    return redirect('home')