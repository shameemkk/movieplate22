"""
URL configuration for moviePlate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path
from user import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('movie.urls')),
    path("signup_page/",views.userRegistration,name='signup'),
    path("login_page/",views.loginpage,name='login'),
    path("update_profile/",views.updateprofile,name='updateprofile'),
    path("",views.home,name='home'),
    path("dashboard/",views.dashbord,name='dashboard'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)