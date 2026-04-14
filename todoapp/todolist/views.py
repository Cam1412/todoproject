from django.shortcuts import render, redirect
from .models import tache
from .forms import TacheForm
from django.contrib import messages


# Create your views here.
def index(request):
    #vérifier la méthode HTTP
    if request.method == "POST":
        # instancier le formulaire avec les données soumises
        form = TacheForm(request.POST) # tacheform vient du fichier forms.py, request.POST contient les données soumises par le formulaire
        #tester la validité du formulaire
        if form.is_valid():
            #enregistrer la tâche dans la base de données
            form.save()
            messages.success(request, "Tâche ajoutée avec succès !") #afficher un message de succès à l'utilisateur
            #redirection vers la page d'accueil
            return redirect('page-home')
    else:
        form = TacheForm() #si la méthode n'est pas POST, on affiche un formulaire vide
    taches = tache.objects.all()  #récupérer toutes les tâches de la base de données  
    return render(request, 'base.html', context={'taches': taches, 'tache_form': form}) #passer les tâches et le formulaire à la template base.html pour l'affichage


def update_tache(request, tache_id):
    tache_a_modifier = tache.objects.get(id=tache_id) #récupérer la tâche à modifier à partir de son ID
    if request.method == "POST":
        form = TacheForm(request.POST, instance=tache_a_modifier) #instancier le formulaire avec les données soumises et l'instance de la tâche à modifier
        if form.is_valid():
            form.save() #enregistrer les modifications dans la base de données
            messages.success(request, "Tâche modifiée avec succès !") #afficher un message de succès à l'utilisateur
            return redirect('page-home') #redirection vers la page d'accueil
    else:
        form = TacheForm(instance=tache_a_modifier) #si la méthode n'est pas POST, on affiche un formulaire pré-rempli avec les données de la tâche à modifier
    return render(request, 'update_tache.html', context={'update_form': form}) #passer le formulaire à la template update_tache.html pour l'affichage

def supprimer_tache(request, tache_id):
    tache_a_supprimer = tache.objects.get(id=tache_id) #récupérer la tâche à supprimer à partir de son ID
    if request.method == "POST":
        tache_a_supprimer.delete() #supprimer la tâche de la base de données
        messages.success(request, "Tâche supprimée avec succès !") #afficher un message de succès à l'utilisateur
        return redirect('page-home') #redirection vers la page d'accueil
    else:
        form = TacheForm(instance=tache_a_supprimer) #si la méthode n'est pas POST, on affiche un formulaire pré-rempli avec les données de la tâche à supprimer pour confirmation de la suppression
    return render(request, 'supprimer_tache.html', context={'tache': tache_a_supprimer, 'suppression_form': form}) #passer la tâche et le formulaire à la template supprimer_tache.html pour l'affichage
