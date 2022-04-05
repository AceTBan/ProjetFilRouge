from django.shortcuts import HttpResponse, render
from . models import *
# def index(request):
#     return HttpResponse("Bienvenue sur mon site AceDeveloppeur ^^")

def accueil(request):
    dernier_annonce = Annonce.objects.order_by('id')
    context = {'annonce_list': dernier_annonce}
    return render(request, 'AceDev/accueil.html', context)

def formulaire(request):
    return render(request, 'AceDev/formulaire.html')

def annonce(request):
    return render(request, 'AceDev/annonce.html')

def cvtheque(request):
    return render(request, 'AceDev/cvtheque.html')

def offres(request):
    return render(request, 'AceDev/offres.html')

def profil(request):
    return render(request, 'AceDev/profil.html')

def service(request):
    return render(request, 'AceDev/service.html')

def utilisateur(request):
    return render(request, 'AceDev/utilisateur.html')

def accueilPro(request):
    dernier_annonce = Annonce.objects.order_by('id')
    context = {'annonce_list': dernier_annonce}
    return render(request, 'AceDev/accueilPro.html', context)