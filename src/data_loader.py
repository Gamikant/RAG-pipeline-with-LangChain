from pathlib import Path
from typing import List, Any
from langchain_community.document_loaders import PyPDFLoader, TextLoader, CSVLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders import UnstructuredExcelLoader
from langchain_community.document_loaders import JSONLoader

def load_all_documents(data_dir: str) -> List[Any]:
    """
    Load all supported files from the data directoy and convert to LangChaain document structure
    Supported: PDF, TXT, CSV, DOCX, Excel, Word, JSON
    """
    # Use project root data folder
    data_path = Path(data_dir).resolve()
    print(f"[DEBUG] Data path: {data_path}")
    documents = []

    # PDF files
    pdf_files = list(data_path.glob("**/*.pdf"))
    print(f"[DEBUG] Found {len(pdf_files)} PDF files: {[str(f) for f in pdf_files]}")
    for pdf_file in pdf_files:
        print(f"[DEBUG] Loading PDF: {pdf_file}")
        try:
            loader = PyPDFLoader(str(pdf_file))
            loaded = loader.load()
            print(f"[DEBUG] Loaded {len(loaded)} PDF docs from {pdf_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[ERROR] Failed to load PDF {pdf_file}: {e}")

    # Text files
    text_files = list(data_path.glob("**/*.txt"))
    print(f"[DEBUG] Found {len(text_files)} text files: {[str(f) for f in text_files]}")
    for text_file in text_files:
        print(f"[DEBUG] Loading text file: {text_file}")
        try:
            loader = TextLoader(str(text_file))
            loaded = loader.load()
            print(f"[DEBUG] Loaded {len(loaded)} text docs from {text_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[ERROR] Failed to load text file {text_file}: {e}")

    # CSV files
    csv_files = list(data_path.glob("**/*.csv"))
    print(f"[DEBUG] Found {len(csv_files)} CSV files: {[str(f) for f in csv_files]}")
    for csv_file in csv_files:
        print(f"[DEBUG] Loading CSV file: {csv_file}")
        try:
            loader = CSVLoader(str(csv_file))
            loaded = loader.load()
            print(f"[DEBUG] Loaded {len(loaded)} CSV docs from {csv_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[ERROR] Failed to load CSV file {csv_file}: {e}")

    # sql files


    return documents