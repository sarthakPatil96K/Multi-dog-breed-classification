from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_view, name='upload'),  # ✅ file upload logic
    path('results/', views.results_view, name='results_view'),
    path('save-history/', views.save_history, name='save_history'),
]
