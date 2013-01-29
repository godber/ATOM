from django.conf.urls.defaults import *
from djangoblog.blog.models import Entry

urlpatterns = patterns('djangoblog.blog.views',
	(r'^$', 'list'),
)
