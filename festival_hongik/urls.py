"""festival_hongik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import account.views
import festival_main.views
import flea_market.views
import lost.views
import publicity.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', festival_main.views.home, name='home'),
    path('line_up/', festival_main.views.line_up, name='line_up'),
    path('line_up_en/', festival_main.views.line_up_en, name='line_up_en'),
    path('line_up_art/', festival_main.views.line_up_art, name='line_up_art'),
    path('map/', festival_main.views.map, name='map'),
    path('store/', festival_main.views.store, name='store'),
    path('drink/', festival_main.views.drink, name='drink'),
    path('toilet/', festival_main.views.toilet, name='toilet'),
    path('contact/', festival_main.views.contact, name='contact'),


    path('signup/', account.views.signup, name='signup'),
    path('login/', account.views.login, name='login'),
    path('logout/', account.views.logout, name = 'logout'),
    
    path('flea_main/', flea_market.views.flea_main, name='flea_main'),
    path('flea_main/<int:flea_market_id>/', flea_market.views.flea_detail, name='flea_detail'),
    path('flea_main/flea_create/', flea_market.views.flea_create, name='flea_create'),
    path('flea_main/flea_new/', flea_market.views.flea_marketpost, name='flea_marketpost'),

    path('lost_main/', lost.views.lost_main, name='lost_main'),
    path('lost_detail/', lost.views.lost_detail, name='lost_detail'),
    path('lost_new/', lost.views.lost_new, name='lost_new'),

    path('publicity_main/', publicity.views.publicity_main, name = 'publicity_main'),
    path('publicity/publicity_detail/<int:publicity_id>/', publicity.views.publicity_detail, name = 'publicity_detail'),
    path('publicity/new', publicity.views.publicity_post, name = 'publicity_new'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
