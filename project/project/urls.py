from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^users_and_blogs/', include('users.urls', namespace='users')),
    url(r'^', include('blogs.urls', namespace='blogs')),
]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)