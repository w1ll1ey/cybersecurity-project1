from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from notes.models import Note

class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()

        user, created = User.objects.get_or_create(username='alice')
        user.set_password('redqueen')
        user.save()

        if created:
            Note.objects.create(name='Alice private note 1', content='Bob should not see this 1', creator=user)
            Note.objects.create(name='Alice private note 2', content='Bob should not see this 2', creator=user)
            
        user, created = User.objects.get_or_create(username='bob')
        user.set_password('squarepants')
        user.save()

        if created:
            Note.objects.create(name='Bob private note 1', content='Alice should not see this 1', creator=user)
            Note.objects.create(name='Bob private note 2', content='Alice should not see this 2', creator=user)
