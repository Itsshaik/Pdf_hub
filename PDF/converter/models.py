from django.db import models
from django.utils import timezone
import os

class ProcessedFile(models.Model):
    OPERATION_CHOICES = [
        ('image_to_pdf', 'Image to PDF'),
        ('pdf_merge', 'PDF Merge'),
        ('pdf_password', 'PDF Password Protection'),
        ('pdf_to_ppt', 'PDF to PowerPoint'),
        ('ocr_extraction', 'OCR Text Extraction'),
    ]
    
    operation = models.CharField(max_length=20, choices=OPERATION_CHOICES)
    original_file = models.FileField(upload_to='uploads/')
    processed_file = models.FileField(upload_to='processed/', blank=True, null=True)
    extracted_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    file_size = models.IntegerField(default=0)
    is_processed = models.BooleanField(default=False)
    error_message = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.operation} - {self.original_file.name}"
    
    def delete(self, *args, **kwargs):
        # Delete physical files when model instance is deleted
        if self.original_file and self.original_file.name:
            try:
                if os.path.isfile(self.original_file.path):
                    os.remove(self.original_file.path)
            except (ValueError, OSError):
                pass
        if self.processed_file and self.processed_file.name:
            try:
                if os.path.isfile(self.processed_file.path):
                    os.remove(self.processed_file.path)
            except (ValueError, OSError):
                pass
        return super().delete(*args, **kwargs)
