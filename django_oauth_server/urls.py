from django.contrib import admin
from django.urls import path, include

from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider'), name='o')
]
