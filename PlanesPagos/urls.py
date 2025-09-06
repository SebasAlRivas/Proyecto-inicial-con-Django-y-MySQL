from django.urls import path,include
from PlanesPagos import views

urlpatterns = [
    path('',views.Index,name="Index.html"),
]