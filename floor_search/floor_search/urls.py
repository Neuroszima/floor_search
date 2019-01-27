"""floor_search URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, re_path

from floor_search.settings import DEBUG, STATIC_ROOT, STATIC_URL
from django.conf.urls import static
from django.contrib import admin
from scrappy.views import crawl
from frontend import views

urlpatterns = [
    path('', views.MainView.as_view()),
    path('admin/', admin.site.urls),
    path('api/crawl/', crawl, name='crawl'),
    path('main', views.MainView.as_view(), name='main'),
    path('run_spider/', views.SpiderFormView.as_view(), name='run_spider'),
    # path('contact/', views.ContactView.as_view(), name='contact'),
    # path('about/', views.AboutView.as_view(), name='about'),
    path('raw/', views.RawDataView.as_view(), name='raw'),
]

# This is required for static files while in development mode. (DEBUG=TRUE)
# No, not relevant to scrapy or crawling :)
if DEBUG:
    urlpatterns += static.static(STATIC_URL, document_root=STATIC_ROOT)
