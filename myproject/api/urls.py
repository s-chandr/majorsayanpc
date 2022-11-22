from django.urls import path
from . import views
from django.urls import include
urlpatterns = [
    
    path('',views.getData),
    path('add/',views.postData),

    

]