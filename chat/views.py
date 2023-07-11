from django.shortcuts import render
from .models import Message

def index(request):
    if request.method == 'POST':
        print("Received data " + request.POST['textmessage'])
        Message.objects.create(text=request.POST['textmessage'], chat=None, author=request.user, receiver=request.user)
    return render(request, 'chat/index.html', {'username': 'Max'} )
