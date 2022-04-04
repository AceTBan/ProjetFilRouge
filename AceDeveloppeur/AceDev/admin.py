from django.contrib import admin
from .models import Utilisateur,Categorie,Annonce,Commentaire,Droit

# Register your models here.
admin.site.register(Utilisateur)
admin.site.register(Categorie)
admin.site.register(Annonce)
admin.site.register(Commentaire)
admin.site.register(Droit)