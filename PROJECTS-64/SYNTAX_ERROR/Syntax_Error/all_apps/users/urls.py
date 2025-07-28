from django.urls import path
from all_apps.users.views import *

urlpatterns=[
    path('',home,name="home"),
    path('sign-up/',sign_up,name="sign-up"),
    path('sign-in/',sign_in,name="sign-in"),
    path('profile/', profile, name="profile"),
    path('profiles/update/<int:pk>/', ProfileUpdateView.as_view(), name='profile_update'),
    path('user-logout/',user_logout,name='user-logout'),
    path('stats/',stats,name="stats"),
    path('view-stats/', view_stats, name='view-stats'),


    
]