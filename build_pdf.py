import os
import subprocess
import re
import shutil

def run_build():
    paper_dir = r"d:\TARS\TarsEx\paper"
    build_dir = os.path.join(paper_dir, "build")
    os.makedirs(build_dir, exist_ok=True)
    os.makedirs(os.path.join(paper_dir, "generated"), exist_ok=True)
    
    print("Running PDFLaTeX (Pass 1)...")
    res1 = subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "-output-directory=build", "main.tex"],
        cwd=paper_dir, capture_output=True, text=True
    )
    
    print("Running BibTeX...")
    # Bibtex requires searching aux file in build
    res_bib = subprocess.run(
        ["bibtex", "build/main"],
        cwd=paper_dir, capture_output=True, text=True
    )
    print(res_bib.stdout)
    print(res_bib.stderr)
    
    print("Running PDFLaTeX (Pass 2)...")
    res2 = subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "-output-directory=build", "main.tex"],
        cwd=paper_dir, capture_output=True, text=True
    )
    
    print("Running PDFLaTeX (Pass 3)...")
    res3 = subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "-output-directory=build", "main.tex"],
        cwd=paper_dir, capture_output=True, text=True
    )
    
    log_path = os.path.join(build_dir, "main.log")
    if os.path.exists(log_path):
        with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
            log_content = f.read()
            
        undefined_citations = re.findall(r"LaTeX Warning: Citation `.*?' on page .*? undefined", log_content)
        undefined_references = re.findall(r"LaTeX Warning: Reference `.*?' on page .*? undefined", log_content)
        missing_figures = re.findall(r"File `.*?' not found", log_content)
        
        print("\n================== BUILD LOG AUDIT ==================")
        print(f"Undefined Citations: {len(undefined_citations)}")
        for uc in undefined_citations:
            print(f"  - {uc}")
            
        print(f"Undefined References: {len(undefined_references)}")
        for ur in undefined_references:
            print(f"  - {ur}")
            
        print(f"Missing Figures/Files: {len(missing_figures)}")
        for mf in missing_figures:
            print(f"  - {mf}")
            
        pdf_path = os.path.join(build_dir, "main.pdf")
        if os.path.exists(pdf_path):
            print("\nBUILD SUCCESSFUL! main.pdf is at:", pdf_path)
            shutil.copy(pdf_path, os.path.join(paper_dir, "main.pdf"))
            print("Copied final PDF to paper/main.pdf")
        else:
            print("\nBUILD FAILED: main.pdf not found in build directory.")
    else:
        print("\nBUILD FAILED: main.log not found.")

if __name__ == "__main__":
    run_build()
