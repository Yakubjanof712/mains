from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send_email/', views.send_email, name='send_email'),
    path('add_data/', views.add_data, name='add_data'),
    path('update_data/<int:data_id>/', views.update_data, name='update_data'),
    path('delete_data/<int:data_id>/', views.delete_data, name='delete_data'),
    path('add_data/', views.add_data, name='add_data'),
    path('update_data/<int:data_id>/', views.update_data, name='update_data'),
    path('delete_data/<int:data_id>/', views.delete_data, name='delete_data'),

]



