from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('abc',views.marks),
    path('def',views.details,name='details'),
    path('admin/', admin.site.urls),
    path('',include("apps.urls")),
    path('',views.home,name='home_page')
]


