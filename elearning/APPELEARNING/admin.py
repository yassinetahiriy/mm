from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import utilisateur, Profile , Matiere1Bac, Niveau, Cours1Bac, Chapitre



@admin.register(Chapitre)
class ChapitreAdmin(admin.ModelAdmin):
    list_display = ['cours', 'titre', 'contenu']



@admin.register(Matiere1Bac)
class Matiere1BacAdmin(admin.ModelAdmin):
    list_display = ['nom', 'description', 'niveau']


@admin.register(Niveau)
class NiveauAdmin(admin.ModelAdmin):
    list_display = ['nom']
    
@admin.register(Cours1Bac)
class Cours1BacsAdmin(admin.ModelAdmin):
    list_display = ['matiere', 'titre']




class UtilisateurAdmin(UserAdmin):
    model = utilisateur
    list_display = ('email', 'prenom', 'nom', 'is_admin', 'is_staff')
    search_fields = ('email', 'prenom', 'nom')
    readonly_fields = ('id',)

    ordering = ('email',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informations personnelles', {'fields': ('prenom', 'nom')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active', 'is_superuser')}),
    )

admin.site.register(utilisateur, UtilisateurAdmin)
admin.site.register(Profile)

