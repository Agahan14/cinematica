from django.contrib import admin
from django.urls import path, include

from users.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),
    path('movies/', include('movies.urls')),
    path('purchase/', include('tickets.urls')),
    path('', RegisterView.as_view()),
]
