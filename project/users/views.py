from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Users
from blogs.models import Record

class BlogsListView(ListView):
    model = Users
    context_object_name = 'users'
    template_name = 'users/users_and_blogs.html'

@login_required
def subscribe(request, pk):
    subscriber = Users.objects.get(id=request.user.id)
    author = Users.objects.get(id=pk)
    if author in  subscriber.subscribes.all():
        subscriber.subscribes.remove(author)
    else:
        subscriber.subscribes.add(author)
    return HttpResponse('Ok')


@login_required
def mark_viewed(request, pk):
    user = Users.objects.get(id=request.user.id)
    record = Record.objects.get(id=pk)
    user.viewed_records.add(record)
    return HttpResponse('Ok')