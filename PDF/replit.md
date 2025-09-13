# PDF Processor

## Overview

PDF Processor is a Django-based web application that provides comprehensive PDF processing capabilities. The application allows users to perform various document operations including image-to-PDF conversion, PDF merging, password protection, PDF-to-PowerPoint conversion, and OCR text extraction from images. It features a clean, Bootstrap-powered interface with file upload functionality and processing history tracking.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Web Framework
- **Django 5.2.6**: Chosen as the primary web framework for its robust MVC architecture, built-in admin interface, and comprehensive security features
- **Single App Structure**: Uses a `converter` app to handle all PDF processing operations, keeping the codebase organized and maintainable
- **Template-based Rendering**: Server-side HTML rendering with Django templates for consistent UI across all pages

### Database Design
- **Django ORM with SQLite**: Uses Django's default SQLite database for development simplicity
- **ProcessedFile Model**: Central model tracking all file operations with fields for operation type, file paths, processing status, and error handling
- **File Management**: Implements custom delete methods to ensure physical file cleanup when database records are removed

### File Processing Architecture
- **Multiple Processing Pipelines**: Separate view functions for each operation type (image-to-PDF, PDF merge, password protection, PDF-to-PowerPoint, OCR)
- **Temporary File Handling**: Uses Python's tempfile module and BytesIO for memory-efficient processing
- **File Storage**: Django's default file storage system with organized upload directories (`uploads/` for originals, `processed/` for outputs)

### Frontend Architecture
- **Bootstrap 5.1.3**: Responsive CSS framework for consistent UI components and mobile compatibility
- **Font Awesome 6.0**: Icon library for enhanced visual interface
- **Custom CSS**: Additional styling for upload areas, hover effects, and card-based layouts
- **Progressive Enhancement**: JavaScript for file selection feedback and clipboard functionality

### Processing Libraries Integration
- **PIL (Pillow)**: Image manipulation and format conversion
- **PyPDF2**: PDF reading, merging, and password protection
- **python-pptx**: PowerPoint presentation generation
- **pytesseract**: OCR text extraction from images
- **reportlab**: PDF generation from images
- **pdf2image**: PDF-to-image conversion for PowerPoint slides

### URL Routing Strategy
- **RESTful URLs**: Clean URL patterns for each operation type
- **File Download Endpoint**: Secure file serving with ID-based access
- **History Tracking**: Dedicated endpoint for viewing processing history

### Security Considerations
- **CSRF Protection**: Django's built-in CSRF middleware enabled
- **File Type Validation**: Accept parameters on file inputs to restrict upload types
- **Error Handling**: Comprehensive exception handling with user-friendly error messages
- **Debug Mode**: Currently enabled for development (should be disabled in production)

## External Dependencies

### Python Libraries
- **Django 5.2.6**: Web framework and ORM
- **Pillow**: Image processing and manipulation
- **PyPDF2**: PDF file operations
- **python-pptx**: PowerPoint file generation
- **pytesseract**: OCR text extraction
- **reportlab**: PDF creation and manipulation
- **pdf2image**: PDF to image conversion

### Frontend Dependencies (CDN)
- **Bootstrap 5.1.3**: CSS framework from jsdelivr CDN
- **Font Awesome 6.0**: Icon library from cdnjs CDN

### System Dependencies
- **Tesseract OCR**: Required by pytesseract for text extraction functionality
- **Poppler Utils**: Required by pdf2image for PDF to image conversion

### File Storage
- **Local File System**: Django's default file storage for uploaded and processed files
- **Static Files**: Bootstrap and Font Awesome served via CDN, custom CSS served locally

### Development Dependencies
- **SQLite**: Default Django database for development
- **Django Development Server**: Built-in server for local development and testing