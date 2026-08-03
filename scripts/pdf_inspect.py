import fitz  # PyMuPDF
import sys
import json
from pathlib import Path

def inspect_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        
        # Basic Metadata
        meta = doc.metadata
        
        # General Info
        info = {
            "filename": Path(pdf_path).name,
            "pages": len(doc),
            "metadata": meta,
            "text_content": []
        }
        
        # Extract text from first few pages (to avoid overwhelming the agent)
        # We'll extract all text but provide a summary if it's too long
        full_text = ""
        for page in doc:
            full_text += page.get_text()
            
        info["text_content"] = full_text
        
        return info
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Missing PDF path argument"}))
        sys.exit(1)
        
    pdf_file = sys.argv[1]
    result = inspect_pdf(pdf_file)
    print(json.dumps(result, ensure_ascii=False, indent=2))
