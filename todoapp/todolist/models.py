from django.db import models

# Create your models here.
class tache(models.Model):
    titre = models.CharField(max_length=250)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_echeance = models.DateTimeField()
    STATUS_CHOICES = ['En cours','Annulée','Terminée']
    status = models.CharField(max_length=20, choices=[(choice, choice) for choice in STATUS_CHOICES], default='En cours')

    def __str__(self):
        return self.titre
    