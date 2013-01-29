from djangoblog.blog.models import Entry
from django.shortcuts import render_to_response

def list(request):
    latest = Entry.objects.filter(status=1)
    return render_to_response('blog/list.html', {
        'latest': latest,
    })
