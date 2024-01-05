from django.urls import path,include
from Auth import views

urlpatterns = [
    path('login/',views.log_in,name='login'),
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    (r'^auth/', include('rest_framework_social_oauth2.urls')),
]
