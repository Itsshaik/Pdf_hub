from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('image-to-pdf/', views.image_to_pdf_view, name='image_to_pdf'),
    path('pdf-merge/', views.pdf_merge_view, name='pdf_merge'),
    path('pdf-password/', views.pdf_password_view, name='pdf_password'),
    path('pdf-to-ppt/', views.pdf_to_ppt_view, name='pdf_to_ppt'),
    path('ocr-extraction/', views.ocr_extraction_view, name='ocr_extraction'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
    path('history/', views.file_history, name='file_history'),
]