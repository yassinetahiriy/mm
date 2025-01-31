from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    niveau = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Profile de {self.user.prenom} {self.user.nom}"


class UtilisateurManager(BaseUserManager):
    def create_user(self, email, prenom, nom, password=None):
        if not email:
            raise ValueError("L'adresse email est obligatoire")
        email = self.normalize_email(email)
        user = self.model(email=email, prenom=prenom, nom=nom)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, prenom, nom, password):
        user = self.create_user(email=email, prenom=prenom, nom=nom, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class utilisateur(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UtilisateurManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['prenom', 'nom']

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin


@receiver(post_save, sender=utilisateur)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=utilisateur)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()




class Niveau(models.Model):
    nom = models.CharField(max_length=255, unique=True)  # Nom de la matière

    def __str__(self):
        return self.nom


class Matiere1Bac(models.Model):
    nom = models.CharField(max_length=255, unique=True)  # Nom de la matière
    description = models.TextField(blank=True, null=True)  # Description facultative
    niveau = models.ForeignKey(
        Niveau, 
        related_name="matieres", 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
    )


    def __str__(self):
        return f"{self.nom} ({self.niveau.nom if self.niveau else 'Aucun niveau'})"



class Cours1Bac(models.Model):
    matiere = models.ForeignKey(Matiere1Bac, related_name="cours", on_delete=models.CASCADE)  # Relation avec Matiere1Bac
    titre = models.CharField(max_length=255)  # Titre du cours
    description = models.TextField(blank=True, null=True)  # Description ou contenu du cours
    video = models.FileField(upload_to="videos/", blank=True, null=True)  # Upload de vidéos

    def __str__(self):
        return f"{self.titre} ({self.matiere.nom})"
    

class Chapitre(models.Model):
    cours = models.ForeignKey(Cours1Bac, related_name="chapitres", on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)  # Titre du chapitre
    contenu = models.TextField()  # Contenu du chapitre

    def __str__(self):
        return f"{self.titre} ({self.cours.titre})"
