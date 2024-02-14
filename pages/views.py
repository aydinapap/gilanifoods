from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# code home asli
class HomePageView(TemplateView):
    template_name = "pages/home.html"


# this is class for rahnama
class AboutPageView(TemplateView):
    template_name = "pages/about.html"


# this is code for post app
class PostListView(TemplateView):
    template_name = "pages/list.html"


# #this is for ordak vavishka link
class OrdakVavishkaPageView(TemplateView):
    template_name = "pages/html/اردک واویشکا.html"

#this is for Anar bij link
class AnarBijPageView(TemplateView):
    template_name = "pages/html/انار بیج.html"

#this is for Baghali ghatogh link
class BaghaliGhatoghPageView(TemplateView):
    template_name = "pages/html/باقالی قاتوق.html"


#this is for Torsh tare link
class TorshTarePageView(TemplateView):
    template_name = "pages/html/ترش تره.html"


#this is for Jaghol maghol link
class JagholMagholPageView(TemplateView):
    template_name = "pages/html/جغول مغول.html"


#this is for sir ghaliye link
class SirGhaliyePageView(TemplateView):
    template_name = "pages/html/سیر قلیه.html"


#this is for fesenjan link
class FesenjoonPageView(TemplateView):
    template_name = "pages/html/فسنجون.html"


#this is for kal kabab link
class KalKababPageView(TemplateView):
    template_name = "pages/html/کال کباب.html"


#this is for mirza ghasemi link
class MirzaGhasemiPageView(TemplateView):
    template_name = "pages/html/میرزاقاسمی.html"

