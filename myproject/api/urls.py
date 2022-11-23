from django.urls import path
from . import views
from django.urls import include
urlpatterns = [
    
    #all gets
    path('getPayment/',views.getPayment),
    path('getShop/',views.getShop),
    path('getReview/',views.getReview),
    path('getCustomer/',views.getCustomer),
    path('getOrder/',views.getOrder),

    #all post
    path('postPayment/',views.postPayment),
    path('postShop/',views.postShop),
    path('postReview/',views.postReview),
    path('postCustomer/',views.postCustomer),
    path('postOrder/',views.postOrder),

]