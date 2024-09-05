from django.urls import path
from .views import add_recipes,view_recipes,delete_recipes,update_recipes,signup_page,login_page,logout_page
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('add-recipes/', add_recipes, name='add-recipes'),
    path('view-recipes/', view_recipes, name='view-recipes'),
    path('delete-recipes/<id>/', delete_recipes, name='delete-recipes'),
    path('update-recipes/<id>/', update_recipes, name='update-recipes'),
    path('signup_page/', signup_page, name='signup-page'),
    path('', login_page, name='login-page'),
    path('logout/', logout_page, name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()