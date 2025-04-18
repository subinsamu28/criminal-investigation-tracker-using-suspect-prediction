"""crime URL Configuration

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
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',views.first),
    path('index',views.index),
    path('reg',views.reg),
    path('index',views.index),
    path('addreg',views.addreg),
    path('logint',views.logint,name="logint"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('addcomplaint',views.addcomplaint,name="addcomplaint"),
    path('adddept',views.adddept,name="adddept"),
    path('viewusers',views.viewusers,name="viewusers"),
    path('viewcompts',views.viewcompts,name="viewcompts"),
    path('crimi',views.crimi,name="crimi"),
    path('dash',views.dash,name="dash"),
    path('dashdept',views.dashdept,name="dashdept"),
    path('viewcriminal',views.viewcriminal,name="viewcriminal"),
    path('viewcrimfilter',views.viewcrimfilter,name="viewcrimfilter"),
    path('addstation',views.addstation,name="addstation"),

    
    path('viewdept',views.viewdept,name="viewdept"),
    
    
    path('addfir',views.addfir,name="addfir"),
    path('viewfirr',views.viewfirr,name="viewfirr"),
    path('viewfirrfilter',views.viewfirrfilter,name="viewfirrfilter"),
    
    
    path('addstud',views.addstud,name="addstud"),
    
    
    path('viewstudfir',views.viewstudfir,name="viewstudfir"),
    path('viewstudfirfilter',views.viewstudfirfilter,name="viewstudfirfilter"),
    path('stud',views.stud,name="stud"),
    path('viewwstud',views.viewwstud,name="viewwstud"),
    path('studaccept/<int:id>',views.studaccept,name='studaccept'),
    path('studreject/<int:id>',views.studreject,name='studreject'),
    
    path('addcriminal',views.addcriminal,name="addcriminal"),
    path('viewcomp',views.viewcomp,name="viewcomp"),
    path('useraccept/<int:id>',views.useraccept,name='useraccept'),
    path('userreject/<int:id>',views.userreject,name='userreject'),
    path('viewcriminalprofile',views.viewcriminalprofile,name='viewcriminalprofile'),
    
    
    
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
