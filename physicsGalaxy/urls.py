"""physicsGalaxy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from os import name

from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from physicsGalaxy import views as index_views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('about_us',views.about, name="about"),
    # path('contact_us',views.contact, name='contact'),
    path('send_data',views.send_data, name="send"),
    path('visit_home',views.home,name="home"),
    path('contactData', include('contactData.urls')),
    path('study_material', include('studyMaterials.urls')),
    path('exam',include('examApp.urls')),
    path('special_exam', include('quizes.urls', namespace='quizes')),
    # path('log_in',index_views.login)
   
	path('log_in', index_views.login, name="log_in"),
    path('log_in_to_quiz',index_views.logintoquiz, name="log_in_to_quiz"),
    path('Sing_Up',index_views.singUp,name="Sing_Up"),
    
	path('singup',index_views.handleSingUp,name="singup"),
    path('login',index_views.handleLogIn,name="singup"),
    path('logout',index_views.handleLogOut,name="singup"),
    path('user_page',index_views.userPage,name="user_page"),
  
    

    url(r'^admin/', admin.site.urls),
   
    url('^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT})
    
    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

