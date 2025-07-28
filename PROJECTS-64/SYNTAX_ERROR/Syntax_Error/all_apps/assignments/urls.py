from django.urls import path
from all_apps.assignments.views import *
urlpatterns = [
    path('all-assignment/',all_assi,name="all-assignment"),
    path('all-projects/',all_projects,name="all-projects"),
    path('upload-files/',upload_files.as_view(),name="upload-files"),
    path('add-category/',add_category.as_view(),name="add-category"),
    
]
