import fitz  # PyMuPDF
import json
import os
import datetime
from sentence_transformers import SentenceTransformer, util

# Load model once
model = SentenceTransformer('all-MiniLM-L6-v2')

# ---------- USER INPUT ----------
input_folder = "./pdfs"  # Put your PDFs in this folder
persona = "PhD Researcher in Computational Biology"
job = "Prepare a comprehensive literature review focusing on methodologies, datasets, and performance benchmarks"
# --------------------------------

# Combine Persona + Job
query = f"{persona}. {job}"

def extract_text_by_page(pdf_path):
    doc = fitz.open(pdf_path)
    pages = []
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text()
        if len(text.strip()) > 100:  # Skip empty pages
            pages.append({"page_number": page_num, "text": text})
    return pages

def rank_pages_by_relevance(pages):
    results = []
    for page in pages:
        score = util.cos_sim(model.encode(query), model.encode(page["text"]))[0][0].item()
        results.append({**page, "score": score})
    sorted_pages = sorted(results, key=lambda x: x["score"], reverse=True)
    return sorted_pages

def generate_output(files, ranked_data):
    extracted_sections = []
    sub_section_analysis = []

    rank = 1
    for item in ranked_data[:5]:  # top 5 important sections
        extracted_sections.append({
            "document": item["document"],
            "page_number": item["page_number"],
            "section_title": "Auto-detected relevant section",
            "importance_rank": rank
        })
        sub_section_analysis.append({
            "document": item["document"],
            "page_number": item["page_number"],
            "refined_text": item["text"][:400].replace('\n', ' ') + "..."  # limit size
        })
        rank += 1

    return {
        "metadata": {
            "input_documents": files,
            "persona": persona,
            "job_to_be_done": job,
            "processing_timestamp": datetime.datetime.now().isoformat()
        },
        "extracted_sections": extracted_sections,
        "sub_section_analysis": sub_section_analysis
    }

def main():
    files = [f for f in os.listdir(input_folder) if f.endswith(".pdf")]
    ranked_results = []

    for file in files:
        full_path = os.path.join(input_folder, file)
        pages = extract_text_by_page(full_path)
        ranked_pages = rank_pages_by_relevance(pages)
        for r in ranked_pages:
            r["document"] = file
        ranked_results.extend(ranked_pages)

    output = generate_output(files, ranked_results)

    with open("challenge1b_output.json", "w") as f:
        json.dump(output, f, indent=4)

    print("✅ Output saved to challenge1b_output.json")

if __name__ == "__main__":
    main()
