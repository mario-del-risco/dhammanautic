from django.contrib import admin
from django.urls import path, include
from . import views
from articles import views as articleviews
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('articles/', include('articles.urls')),
    path('about/', views.about, name='about'),
    path('', articleviews.articles_list , name='home'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
