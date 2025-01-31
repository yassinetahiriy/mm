from django.core.management.base import BaseCommand
from APPELEARNING.models import utilisateur, Profile

class Command(BaseCommand):
    help = 'Crée les profils manquants pour les utilisateurs existants'

    def handle(self, *args, **kwargs):
        users_without_profiles = utilisateur.objects.filter(profile__isnull=True)
        count = 0

        for user in users_without_profiles:
            Profile.objects.create(user=user)
            count += 1

        self.stdout.write(self.style.SUCCESS(f'{count} profils créés avec succès.'))
