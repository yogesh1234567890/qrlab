"""QRLabs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from QRLabs import views
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('loginPage', views.loginPage, name='loginPage'),
    path('login', views.logins, name='login'),
    path('signupPage', views.signupPage, name='signupPage'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logouts, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard/create/save', views.dashboardCreateSave, name='dashboardCreateSave'),
    # path('dashboard/edit/save', views.dashboardEditSave, name='dashboardEditSave'),
    path('dashboard/lock', views.dashboardlock, name='dashboardlock'),
    path('dashboard/unlock', views.dashboardunlock, name='dashboardunlock'),
    path('dashboard/downlaod/<objId>', views.dashboarddownload, name='dashboarddownload'),
    path('dashboard/statics', views.dashboardstatic, name='dashboardstatic'),
    path('dashboard/archived', views.dashboardarchived, name='dashboardarchived'),
    path('dashboard/folders', views.dashboardfolders, name='dashboardfolders'),
    path('archiveObj/<objId>',views.archiveObj,name='archiveObj'),
    path('unarchiveObj/<objId>',views.unarchiveObj,name='unarchiveObj'),
    path('mkstatic/<objId>',views.mkstatic,name='mkstatic'),
    path('mkdynamic/<objId>',views.mkdynamic,name='mkdynamic'),
    path('delfolder/<objId>',views.delfolder,name='delfolder'),
    path('createfolder',views.createfolder,name='createfolder'),
    path('movetofolder/<str:objId>',views.movetofolder,name='movetofolder'),
    path('editFolder/<str:objId>',views.editFolder,name='editFolder'),
    path('viewfolder/<str:objId>',views.viewfolder,name='viewfolder'),
    path('qrtitleset/<str:objId>',views.qrtitleset,name='qrtitleset'),
    path('editcontent/<str:objId>', views.editcontent, name='editcontent'),
    path('editcontent/save/<str:objId>', views.editcontentsave, name='editcontentsave'),
    path('editshape/<str:objId>', views.editshape, name='editshape'),
    path('editshape/save/<str:objId>', views.editshapesave, name='editshapesave'),
    path('getQrCodePreview', views.getQrCodePreview, name='getQrCodePreview'),
    path('preditshapesave/<objId>', views.preditshapesave, name='preditshapesave'),
    path('preditcontentsave/<str:objId>', views.preditcontentsave, name='preditcontentsave'),

    path('qr/<int:id>', views.dynamic_qr_code, name='dynamicqr'),
]


urlpatterns = urlpatterns+static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)
