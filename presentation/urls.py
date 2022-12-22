from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('presentations/<int:pk>', views.presentations_page, name='presentations'),
    path('presentation_detail/', views.presentation_detail_page, name='presentation_detail'),
    
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
]



 
                
 
                







