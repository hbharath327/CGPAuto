from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from typing import List
import os
import shutil
from backend.cgpa_calc import calculate_cgpa_from_pdfs
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify ["http://localhost:5173"] for more security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploaded_pdfs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload")
async def upload_files(files: List[UploadFile] = File(...)):
    file_paths = []
    for file in files:
        file_location = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_location, "wb") as f:
            shutil.copyfileobj(file.file, f)
        file_paths.append(file_location)
    result = calculate_cgpa_from_pdfs(file_paths)
    # Optionally, clean up uploaded files here
    return JSONResponse({
        "message": "CGPA calculated",
        "cgpa": result["cgpa"],
        "sgpas": result["sgpas"],
        "semesters": result["semesters"]
    }) 