from django.shortcuts import render

def websocket_status(request):
    return render(request, 'websocket_status.html')