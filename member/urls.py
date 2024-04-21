from django.contrib import admin
from django.urls import path
from .views import *
from .views import update_thakur





from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home),
    path("add",views.addstu),
    path("delete_thakur/<int:roll>/", delete_thakur),
    path("update_thakur/<int:roll>",update_thakur),
    
    
    
    path("del3",views.del3),

     

]