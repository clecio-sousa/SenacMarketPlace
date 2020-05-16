

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produto/', include('produto.urls')),#url da pagina produto
]
