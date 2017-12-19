from django.shortcuts import render

def index(request):
    template = 'index.html'
    context = {
        'title': "GUARDIAN",
    }
    return render(request, template, context)
