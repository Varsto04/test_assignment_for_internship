from django.apps import apps
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def create_initial_weather(sender, **kwargs):
    if sender.name != 'main':
        return

    Weather = apps.get_model('main', 'Weather')
    if not Weather.objects.exists():
        Weather.objects.bulk_create([
            Weather(city='London', temperature=20),
            Weather(city='Tallinn', temperature=22),
        ])
