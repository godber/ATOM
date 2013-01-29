from lettuce import before, after, world
from django.test import client

@before.all
def setup_browser():
    world.browser = client.Client()
