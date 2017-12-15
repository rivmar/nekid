from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Users

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
        response=0
    else:
        subscriber.subscribes.add(author)
        response=1
    return HttpResponse(response)