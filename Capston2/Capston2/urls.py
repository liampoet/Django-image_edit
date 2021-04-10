"""Capston2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from Capston2.views import HomeView, UserCreateView, UserCreateDoneTV, descriptionView

urlpatterns = [
    path('admin/', admin.site.urls),
    #홈뷰 
    path('', HomeView.as_view(), name='home'), #url 패턴명 = home
    #설명 뷰
    path('description/', descriptionView.as_view(), name='description'),
    # 장고 내장 인증 django.contrib.auth.urls 모듈 가져오기
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),

    # APP_URLCONF 방식
    # Include 함수 이용, 각각 앱쪽의 url에서 처리
    path('upload/', include('ImgSub.urls')),
    path('photo/', include('photo.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
