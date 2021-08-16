from django.urls import path
from  .  import views 
urlpatterns = [
    path('v1/getdata/', views.GetData.as_view(), name='getdata'),
]