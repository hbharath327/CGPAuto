# CraGPAuto: Full-Stack CGPA Calculator

This project is a full-stack web application for calculating CGPA from uploaded marksheet PDFs. It features a FastAPI backend (Python) for PDF parsing and calculation, and a React (Vite) frontend for user interaction and visualization.

---

## Features
- Upload one or more marksheet PDFs
- Automatic extraction of subject marks, credits, and calculation of SGPA/CGPA
- Detailed per-semester and per-subject breakdown
- Modern React frontend
- Ready for team collaboration

---

## Prerequisites

### Backend
- Python 3.9+
- [Ghostscript](https://ghostscript.com/download/gsdnld.html) (optional, only needed for 'lattice' flavor in Camelot)
- Poppler (optional, for some PDF parsing)

### Frontend
- Node.js (v16+ recommended)
- npm

---

## Setup Instructions

### 1. Clone the Repository
```sh
git clone <your-repo-url>
cd CraGPAuto
```

### 2. Backend Setup (FastAPI)

#### a. Create and activate a virtual environment
```sh
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

#### b. Install dependencies
```sh
pip install -r backend/requirements.txt
```

#### c. (Optional, no need as of now) Install Ghostscript
- Download and install from: https://ghostscript.com/download/gsdnld.html
- Add Ghostscript's `bin` directory to your system PATH.
- Not required if using only the 'stream' flavor in Camelot (default in this project).

#### d. Run the backend server
```sh
uvicorn backend.main:app --reload
```
- The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 3. Frontend Setup (React)

```sh
cd cgpauto-frontend
npm install
npm run dev
```
- The frontend will be available at [http://localhost:5173](http://localhost:5173) (default Vite port)

---

## Usage
1. Open the frontend in your browser.
2. Upload one or more marksheet PDFs.
3. View CGPA, SGPA, and detailed semester/subject breakdown.

---

## Troubleshooting
- **CORS errors:** Ensure the backend is running and CORS is enabled (already set up in `main.py`).
- **PDF parsing issues:**
  - Try with different PDFs.
  - Check backend logs for DataFrame output to debug extraction.
  - If using 'lattice' flavor, ensure Ghostscript is installed.
- **Dependency issues:**
  - Double-check Python and Node.js versions.
  - Run `pip install -r backend/requirements.txt` and `npm install` as needed.

---

## Contributing
- Create feature branches for new work.
- Use clear commit messages.
- Open pull requests for review.

---

## License
MIT (or specify your license here)
