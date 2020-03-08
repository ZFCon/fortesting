from django.contrib import admin
from django.urls import path, include

from autocomplete.views import *
from channel.views import index, room

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('api.urls', 'api'), namespace='api')),
    path('pdf/', include(('pdf.urls', 'pdf'), namespace='pdf')),
    path('html/', include(('htmltest.urls', 'html'), namespace='html')),
    path(
        'user/',
        UserAutocomplete.as_view(),
        name='user',
    ),
    path('chat/', index, name='chat'),
    path('chat/<str:room_name>/', room, name='room'),
]
