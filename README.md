# Smart Document Processing

## Nadar Saraswathi College of Engineering and Technology - Team Robust

### Team Members:
- **Vigneshwar S** - Team Leader
- **Karan** - Team Member
- **Sathya Seelan M** - Team Member

### Theme:
Smart Automation and Digital Transformation

### Problem Statement:
Smart Document Processing and Form Filling System

### Description:
Our project focuses on developing a versatile system that aims to automate the process of verifying, processing, and auto-filling various types of documents and forms across multiple industries.

### Key Features:
- **Document Analysis and Extraction:** Extracts information from different document types (e.g., ID cards, utility bills).
- **Verification:** Checks the authenticity and validity of the documents.
- **Auto-Filling:** Automatically fills forms based on extracted data and user inputs.
- **User-Friendly Interface:** Simplifies document submission and form-filling processes.

---

## Smart Document Processing - Setup Guide

### Prerequisites
Ensure you have the following software installed:
- Python (version 3.8+)
- pip (Python package installer)
- Poppler and Tesseract OCR

### Installation Steps
1. **Clone the Repository**

2. **Set Up a Virtual Environment**
   Creating a virtual environment is optional but recommended:
   ```bash
   python -m venv venv
   ```
   Activate the virtual environment:
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**
   Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Poppler**
   - **Windows:** Download from [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/) and add the bin folder to your system's PATH.
   - **macOS/Linux:** Run the following commands:
     ```bash
     brew install poppler  # For macOS
     sudo apt-get install poppler-utils  # For Linux
     ```

5. **Install Tesseract OCR**
   - **Windows:** Download from [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) and add it to your system's PATH.
   - **macOS/Linux:**
     ```bash
     brew install tesseract  # For macOS
     sudo apt-get install tesseract-ocr  # For Linux
     ```

6. **Run the Project**
   Start the application by running:
   ```bash
   python app.py
   ```
   Open your web browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000).

### Features
- **Automatic Document Type Detection:** Upload PDFs or images and have them classified automatically.
- **Confidence Score Feedback:** Alerts users when documents are of poor quality and cannot be processed.

### Troubleshooting
**Unreadable Document Feedback:** If the uploaded document quality is low, a message will guide you to upload a clearer version.

### Additional Information
Store all sensitive information or environment variables in a .env file. Machine Learning models should be placed in the `model/` directory.

### References
For additional documentation or support:
- [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
