from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.decorators import login_required
from .models import utilisateur, Matiere1Bac, Cours1Bac, Niveau, Chapitre


def signup(request):
    if request.method == 'POST':
        prenom = request.POST.get('prenom')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        mot_de_passe = request.POST.get('mot_de_passe')
        confirmer_mot_de_passe = request.POST.get('confirmer_mot_de_passe')
        niveau_id = request.POST.get('niveau')

        # Validation des mots de passe
        if mot_de_passe != confirmer_mot_de_passe:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return redirect('signup')

        # Vérification si l'email existe déjà
        if utilisateur.objects.filter(email=email).exists():
            messages.error(request, "L'email est déjà utilisé.")
            return redirect('signup')

        try:
            # Vérifier si le niveau existe
            niveau = Niveau.objects.get(id=niveau_id)

            # Créer un utilisateur
            user = utilisateur.objects.create_user(
                email=email,
                prenom=prenom,
                nom=nom,
                password=mot_de_passe
            )

            # Assigner le niveau au profil de l'utilisateur
            user.profile.niveau = niveau.nom
            user.profile.save()

            # Connecter automatiquement l'utilisateur
            django_login(request, user)
            messages.success(request, "Compte créé avec succès.")
            return redirect('user_login')
        except Niveau.DoesNotExist:
            messages.error(request, "Niveau invalide.")
            return redirect('signup')

    # Si la requête est GET, afficher le formulaire
    niveaux = Niveau.objects.all()
    return render(request, 'signup.html', {'niveaux': niveaux})


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        mot_de_passe = request.POST.get('password')

        # Authentifier l'utilisateur
        user = authenticate(request, username=email, password=mot_de_passe)
        if user is not None:
            # Connecter l'utilisateur
            django_login(request, user)
            messages.success(request, f"Bienvenue, {user.prenom} !")
            return redirect('accueil')
        else:
            messages.error(request, "Email ou mot de passe incorrect.")
            return redirect('user_login')

    return render(request, 'user_login.html')


@login_required
def accueil(request):
    """
    View for the home page.
    Accessible uniquement aux utilisateurs connectés.
    """
    matieres = Matiere1Bac.objects.all()  # Récupérer toutes les matières
    context = {
        'title': 'Bienvenue sur la plateforme scolaire',
        'description': 'Cette plateforme permet aux étudiants et enseignants de collaborer efficacement, suivre des cours, et accéder à des ressources éducatives.',
        'matieres': matieres  # Inclure les matières dans le contexte
    }
    return render(request, 'accueil.html', context)


@login_required
def cours(request):
    matieres = Matiere1Bac.objects.all()
    return render(request, 'cours.html', {'matieres': matieres})

@login_required
def cours_detail(request, matiere_id):
    matiere = get_object_or_404(Matiere1Bac, id=matiere_id)
    cours_list = Cours1Bac.objects.filter(matiere=matiere)

    # Pour afficher les chapitres d'un cours spécifique
    cours_id = request.GET.get('cours_id')
    selected_cours = None
    chapitres = None

    if cours_id:
        selected_cours = get_object_or_404(Cours1Bac, id=cours_id)
        chapitres = selected_cours.chapitres.all()

    return render(request, 'cours_detail.html', {
        'matiere': matiere,
        'cours_list': cours_list,
        'selected_cours': selected_cours,
        'chapitres': chapitres,
    })


def chapitre_detail(request, chapitre_id):
    chapitre = get_object_or_404(Chapitre, id=chapitre_id)
    return render(request, 'chapitre_detail.html', {'chapitre': chapitre})
    
