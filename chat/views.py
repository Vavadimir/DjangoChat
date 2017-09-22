from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from .models import Comments
from django.utils import timezone


def index(request):
    """Start page (redirecting when is not authenticated)"""

    if request.user.is_authenticated():
        return redirect('choice_page')
    else:
        return render(request, 'chat/index.html')


def pages(request):
    """Redirect to chosen chat if user is authenticated"""

    try:
        name = request.POST['name']
        passw = request.POST['passw']
    except:
        if request.user.is_authenticated():
            return render(request, 'chat/choice_page.html.html')
        else:
            return HttpResponse('Permission denied')
    else:
        user = authenticate(username=name, password=passw)
        if user is not None:
            login(request, user)
            return redirect('choice_page')
        else:
            if name in User.objects.all().values_list('username', flat=True):
                return render(request, 'chat/index.html', {"error_message": "Bad password"})
            else:
                user = User.objects.create_user(username=name, password=passw)
                user = authenticate(username=name, password=passw)
                login(request, user)
                return redirect('choice_page')


def comments(request):
    """Post the new message to a chat"""

    try:
        comm = request.POST['comment']
    except:
        if request.user.is_authenticated():
            return render(request, 'chat/comments.html')
        else:
            return HttpResponse('Permission denied')
    else:
        #comment = Comments.create()
        cmnt = Comments(author=request.user, pub_date=timezone.now(), comment=comm)
        Comments.save(cmnt)
        return redirect('chat')


def chat(request):
    """Get the simple chat"""

    if request.user.is_authenticated():
        return render(request, 'chat/chat.html', {'comments_set': Comments.objects.all()})
    else:
        return redirect('index')


def chatbootstrap(request):
    """Get the real-time chat (instant messaging)"""

    if request.user.is_authenticated():
        s = Comments.objects.all()
        if request.POST:
            comm = request.POST["comm"]
            cmnt = Comments(author=request.user, pub_date=timezone.now(), comment=comm)
            Comments.save(cmnt)
            return render(request, 'chat/chatbootstrap.html', {'comments_set': Comments.objects.all()})
        else:
            return render(request, 'chat/chatbootstrap.html', {'comments_set': s})
    else:
        return redirect('index')


def messages(request):
    """Get all messages in chat"""

    s = Comments.objects.all()
    return render(request, 'chat/messages.html', {'comments_set': s})


def choice_page(request):
    """Choice of chat"""

    if request.user.is_authenticated():
        return render(request, 'chat/choice_page.html')
    else:
        return redirect('index')


def logout_us(request):
    """Logout the active user"""

    logout(request)
    return redirect('index')
