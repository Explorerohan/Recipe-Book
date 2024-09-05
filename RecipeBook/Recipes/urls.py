from django.urls import path
from .views import add_recipes,view_recipes,delete_recipes,update_recipes
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('add-recipes/', add_recipes, name='add-recipes'),
    path('view-recipes/', view_recipes, name='view-recipes'),
    path('delete-recipes/<id>/', delete_recipes, name='delete-recipes'),
    path('update-recipes/<id>/', update_recipes, name='update-recipes'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()