from django.core.management.base import BaseCommand
from mixer.backend.django import mixer

from base_app.models import Item


class Command(BaseCommand):
    help = "Create test data"

    def handle(self, *args, **kwargs):
        items = Item.objects.all().count()
        if items < 10:
            while items < 10:
                item = mixer.blend(Item)
                items = Item.objects.all().count()
            self.stdout.write("Created data x 10")
        else:
            self.stdout.write("Data has already been created")