from django.urls import path
from basicapp import views

app_name = 'basicapp'

urlpatterns = [
    path('another_template/', views.another_template, name = 'another_template'),
    path('third_temp/', views.third, name = 'third')

]
