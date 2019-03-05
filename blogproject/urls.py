"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import blog1.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog1.views.home , name = "home"),
    #path('어떤 url이들어오면', (어디에있는)어떤함수를 실행시켜라)
    path('portfolio/', portfolio.views.portfolio, name = "portfolio"),
    path('portfolio/<int:portfolio_id>', portfolio.views.p_detail, name = "p_detail"),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog1.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

