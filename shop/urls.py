from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns  = [
    path('', views.index, name='index'),
    path('preview/<int:prid>', views.preview, name='preview'),
    path('checkout', views.checkout, name='checkout'),
    path('tracker', views.tracker, name='tracker'),
    path('contactUs', views.contactUs, name='contactUs'),
    path('search', views.search, name='search'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)