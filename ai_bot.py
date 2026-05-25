import os
import google.generativeai as genai
import chromadb
import mysql.connector
from pypdf import PdfReader

# ── Paste your Gemini API key here ──
GEMINI_API_KEY = "AIzaSyDQwyM0Pl21TLm8lJguQxf0lNRb5CMuNz0"

# ── Your MySQL credentials ──
MYSQL_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "your_mysql_password_here",
    "database": "docqa"
}

# ── Configure Gemini ──
genai.configure(api_key=AIzaSyDQwyM0Pl21TLm8lJguQxf0lNRb5CMuNz0)
llm = genai.GenerativeModel("gemini-1.5-flash")

# ── Setup ChromaDB (saves locally in a folder called chroma_db) ──
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="documents")

print("✅ All configured successfully!")