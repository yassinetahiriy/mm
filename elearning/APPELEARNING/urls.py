from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='home'),  # La route racine mène à la page de connexion
    path('user_login/', views.user_login, name='user_login'),
    path('signup/', views.signup, name='signup'),
    path('accueil/', views.accueil, name='accueil'),  # Page d'accueil pour les utilisateurs connectés
    path('cours/', views.cours, name='cours'),
    path('cours/<int:matiere_id>/', views.cours_detail, name='cours_detail'),
    path('chapitre/<int:chapitre_id>/', views.chapitre_detail, name='chapitre_detail'),
]
