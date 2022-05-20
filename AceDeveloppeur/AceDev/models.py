from django.db import models

# Create your models here.
class Utilisateur(models.Model):
    nom_utilisateur=models.CharField(max_length=30)
    prenom_utilisateur=models.CharField(max_length=30)
    login_utilisateur=models.CharField(max_length=30)
    mot_de_passe_utilisateur=models.CharField(max_length=100)
    ville_utilisateur=models.CharField(max_length=50)
    tel_utilisateur=models.CharField(max_length=30)

    def __str__(self):
        affiche = f"{self.nom_utilisateur} {self.prenom_utilisateur}"
        return affiche

class Categorie(models.Model):
    nom_categorie=models.CharField(max_length=50)
    def __str__(self):
        return self.nom_categorie

class Annonce(models.Model):
    titre_annonce=models.CharField(max_length=50)
    contenu_annonce=models.TextField(null=True, blank=True)
    date_crea_annonce= models.DateTimeField("Date de debut d'annonce")
    categorie =models.ManyToManyField(Categorie,blank=True)
    def __str__(self):
        affiche = f"{self.titre_annonce} {self.contenu_annonce} {self.date_crea_annonce} {self.categorie}"
        return affiche


class Commentaire(models.Model):
    contenu_commentaire=models.TextField
    date_commentaire= models.DateTimeField("Date de debut du commentaire")
    def __str__(self):
        affiche = f" {self.contenu_commentaire}  {self.date_commentaire}"
        return affiche 

class Droit(models.Model):
    nom_droit=models.CharField(max_length=30)