from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name= 'homepage'),
    path('delete/<int:id>',views.Delete_record,name='delete'),
    path('<int:id>',views.Update_record,name='update')
]
