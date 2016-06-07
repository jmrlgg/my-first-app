from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
import datetime
from django import template
from django.db import models
from django.db import connection
from FirstApp.models import Blogger, Entry, Blog
from FirstApp.forms import ContactForm, PostForm
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
def foo(request):
    return HttpResponse("Hello Guys!")


def home(request):
    return render(request, 'starter.html', {})

@login_required
def starter(request):
    return render(request, 'starter.html', {})


def base(request):
    return render(request, 'base.html', {})


def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now, 'current_section': 'current_datetime'})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    # html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return render(request, 'hours_ahead.html', {'hour_offset': offset, 'next_time': dt, 'current_section': 'hours_ahead'})

@login_required
def users(request):
    post = Blogger.objects.all()
    return render(request, 'members.html', {'post': post})


@login_required
def entry(request):
    post = Entry.objects.all()
    return render(request, 'post.html', {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pub_date = datetime.datetime.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'post_edit.html', {'form': form})


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Entry, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Entry, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = datetime.datetime.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'jlmassey05@gmail.com'),
                ['jlmassey05@gmail.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})

def contact_popup(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'jlmassey05@gmail.com'),
                ['jlmassey05@gmail.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact_popup.html', {'form': form})
