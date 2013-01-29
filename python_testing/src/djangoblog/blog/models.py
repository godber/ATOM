from django.db import models
from django.contrib.syndication.feeds import Feed
from django.contrib.sitemaps import Sitemap
from datetime import datetime # imported only for test, yuck


class Entry(models.Model):
    """
    The Entry Model represents a single Blog Post.

    >>> e = Entry(title='New Post', slug='new_post', body_html='<h1>hi</h1>', pub_date=datetime.now(), enable_comments=True, status=1)
    >>> e.save()
    >>> e.status
    1
    >>> e.enable_comments
    True
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(
        unique_for_date='pub_date',
        help_text='Automatically built from the title.'
    )
    body_html = models.TextField()
    pub_date = models.DateTimeField('Date published')
    enable_comments = models.BooleanField(default=True)
    PUB_STATUS = (
        (0, 'Draft'),
        (1, 'Published'),
    )
    status = models.IntegerField(choices=PUB_STATUS, default=0)


    class Meta:
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'
        verbose_name_plural = 'entries'

    def __unicode__(self):
        return u'%s' %(self.title)

    def get_absolute_url(self):
        return "/%s/%s/" %(self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)

    def get_previous_published(self):
        return self.get_previous_by_pub_date(status__exact=1)

    def get_next_published(self):
        return self.get_next_by_pub_date(status__exact=1)
