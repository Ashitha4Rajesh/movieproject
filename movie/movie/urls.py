"""
URL configuration for movie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django .conf import settings
from django.conf.urls.static import static
from reviews import views
app_name="reviews"
urlpatterns = [
    path('admin/', admin.site.urls),
      path("addmovie",views.addmovie,name='addmovie'),
      path("v",views.viewmovie,name='viewmovie'),
       path("updel/<int:p>",views.updel,name='updel'),
       path("delete/<int:p>",views.delete,name='delete'),
       path("update/<int:p>",views.update,name='update'),
        path("",views.home,name='home'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)