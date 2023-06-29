from django.shortcuts import render
from django.views.generic import TemplateView
# from django.http import HttpResponse
def index(request):
    # return HttpResponse('Helo world')
    return render(request, 'menu/index.html')
class DonateView(TemplateView):
    template_name = 'menu/Donate.html'
class GameView(TemplateView):
    template_name = 'menu/Games.html'
class SNView(TemplateView):
    template_name = 'menu/sn.html'