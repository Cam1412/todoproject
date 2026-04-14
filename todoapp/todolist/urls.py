from django.urls import path
from .views import index, update_tache, supprimer_tache

urlpatterns = [
    path('',index, name='page-home'),
    path('modifier-tache/<int:tache_id>/', update_tache, name='modifier-tache'),
    path('supprimer-tache/<int:tache_id>/', supprimer_tache, name='supprimer-tache'),
]

