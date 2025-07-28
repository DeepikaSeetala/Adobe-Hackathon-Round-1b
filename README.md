# Persona-Driven Document Intelligence System
## Overview
This project implements a document intelligence system that extracts, analyzes, and ranks content from PDF documents based on relevance to a specific persona and job-to-be-done. The system uses natural language processing techniques to identify the most relevant sections of documents for targeted information retrieval.

## Features
- PDF text extraction with page and section tracking
- Semantic understanding using lightweight transformer models
- Relevance ranking based on persona and job requirements
- Granular subsection analysis for detailed information extraction
- JSON output with ranked sections and subsection analysis
## System Requirements
- Python 3.9+
- CPU-only environment (no GPU required)
- Less than 1GB of memory for model
- No internet access required during execution
## Installation
### Option 1: Using pip
```
pip install -r requirements.txt
```
### Option 2: Using Docker
```
docker build -t 
document-intelligence .
docker run -v /path/to/pdfs:/app/
pdfs document-intelligence
```
## Project Structure
- main.py : Core application logic for document processing and analysis
- requirements.txt : Python dependencies
- Dockerfile : Container configuration for deployment
- approach_explanation.md : Detailed explanation of the methodology
- create_test_pdf.py : Utility to create sample PDF documents for testing
- challenge1b_output.json : Example output format
## How It Works
The system operates in four main stages:
1.
   Document Processing : Extracts text from PDFs using PyPDF2, preserving page numbers and section structure.
2.
   Semantic Understanding : Uses the all-MiniLM-L6-v2 transformer model to create embeddings for document sections and persona descriptions.
3. 
   Relevance Ranking : Calculates cosine similarity between document sections and the persona+job description to rank sections by relevance.
4.
   Subsection Analysis : Performs granular analysis of the most relevant sections to identify specific information.
