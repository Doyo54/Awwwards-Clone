from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    
    re_path(r'^$',views.index,name='index'),
    re_path(r'^api/', views.PostView.as_view()),

]   
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)