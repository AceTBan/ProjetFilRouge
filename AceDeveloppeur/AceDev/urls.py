from django.urls import URLPattern, path
from . import views
app_name = 'AceDev'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.accueil, name='accueil'),
    path('formulaire/', views.formulaire, name='formulaire'),
    path('annonce/', views.annonce, name='annonce'),
    path('cvtheque/', views.cvtheque, name='cvtheque'),
    path('offres/', views.offres, name='offres'),
    path('profil/', views.profil, name='profil'),
    path('service/', views.service, name='service'),
    path('utilisateur/', views.utilisateur, name='utilisateur'),
    path('accueilPro', views.accueilPro, name='accueilPro')


]
