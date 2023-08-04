"""
URL configuration for webkantin project.

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
from django.conf import settings
from django.conf.urls.static import static
from WebKantinAPP.views import Index, Profile
from makanan.views import MenuKantin
from account.views import login_user, register_user, logout_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='home'),
    path('menu/', MenuKantin.as_view(), name='menukantin'),
    path('item/<int:item_id>/', MenuKantin.item_detail, name='item_detail'),
    path('profile/', Profile.as_view(), name='profile'),
    path('login/', login_user, name='login'),
    path('register/', register_user, name='register'),
    path('logout', logout_user, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
