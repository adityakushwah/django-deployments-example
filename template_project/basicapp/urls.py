from django.urls import path
from basicapp import views

app_name = 'basic_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other')

]