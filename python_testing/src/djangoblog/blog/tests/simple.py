"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from djangoblog.blog.models import Entry
from datetime import datetime

class EntryTest(TestCase):
    def test_simple_entry(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        e = Entry(title='New Post', slug='new_post', 
                body_html='<h1>hi</h1>', pub_date=datetime.now(), 
                enable_comments=True, status=1)
        e.save()
        self.assertEqual(1, e.status)
        self.assertEqual(True, e.enable_comments)


# I don't know why anyone would do this, other than doctest being the only
# trick in their bag.
__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}

