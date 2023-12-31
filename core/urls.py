"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from home.views import *
from vege.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
   
   path('home/', home , name="home"),
   path('', login_page , name="home"),
   


   path('success-page/', success_page , name="success_page"),

   path('recipes/', recipes , name="recipes"),
   path('delete-recipe/<id>/', delete_recipe , name="delete_recipe"),
   path('update-recipe/<id>/', update_recipe , name="update_recipe"),
   path('login/', login_page , name="login"),
   path('logout/', logout_page , name="logout"),
   path('register/', register , name="register"),


   path('about/', about , name="about"),

   path('contact/', contact , name="contact"),


   path('students/' , get_students, name='get_students'),
   path('check-marks/<student_id>' , see_marks, name='see_marks'),



    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()