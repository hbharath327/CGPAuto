import camelot
import json
import os

NUMBER_OF_SEMESTERS = 8

SUBJECT_CODE_CREDITS = {
    # Semester 1
    "21MAT11": 3,   # CALCULUS AND DIFFERENTIAL EQUATIONS
    "21PHY12": 3,   # ENGINEERING PHYSICS
    "21ELE13": 3,   # BASIC ELECTRICAL ENGINEERING
    "21CIV14": 3,   # ELEMENTS OF CIVIL ENGINEERING AND MECHANICS
    "21EVN15": 3,   # ENGINEERING VISUALIZATION
    "21PHYL16": 1,  # ENGINEERING PHYSICS LABORATORY
    "21ELEL17": 1,  # BASIC ELECTRICAL ENGINEERING LABORATORY
    "21EGH18": 2,   # COMMUNICATIVE ENGLISH
    "21IDT19": 1,   # INNOVATION AND DESIGN THINKING
    # Semester 2
    "21MAT21": 3,   # ADVANCED CALCULUS AND NUMERICAL METHODS
    "21CHE22": 3,   # ENGINEERING CHEMISTRY
    "21PSP23": 3,   # PROBLEM - SOLVING THROUGH PROGRAMMING
    "21ELN24": 3,   # BASIC ELECTRONICS & COMMUNICATION ENGINEERING
    "21EME25": 3,   # ELEMENTS OF MECHANICAL ENGINEERING
    "21CHEL26": 1,  # ENGINEERING CHEMISTRY LABORATORY
    "21CPL27": 1,   # COMPUTER PROGRAMMING LABORATORY
    "21EGH28": 2,   # PROFESSIONAL WRITING SKILLS IN ENGLISH
    "21SFH29": 1,   # SCIENTIFIC FOUNDATIONS OF HEALTH
    # Semester 3
    "21MAT31": 3,   # TRANSFORM CALCULUS, FOURIER SERIES AND NUMERICAL TECHNIQUES
    "21CS32": 4,    # DATA STRUCTURES AND APPLICATIONS
    "21CS382": 1,   # PROGRAMMING IN C++
    "21CS33": 4,    # ANALOG AND DIGITAL ELECTRONICS
    "21CS34": 3,    # COMPUTER ORGANIZATION AND ARCHITECTURE
    "21CSL35": 1,   # OBJECT ORIENTED PROGRAMMING WITH JAVA LABORATORY
    "21SCR36": 1,   # SOCIAL CONNECT AND RESPONSIBILITY
    "21KSK37": 1,   # SAMSKRUTHIKA KANNADA
    # Semester 4
    "21MATCS41": 3, # MATHEMATICAL FOUNDATIONS FOR COMPUTING, PROBABILITY & STATISTICS
    "21CS42": 4,    # DESIGN AND ANALYSIS OF ALGORITHMS
    "21CSL483": 1,  # R PROGRAMMING
    "21CS43": 4,    # MICROCONTROLLER AND EMBEDDED SYSTEM
    "21CS44": 3,    # OPERATING SYSTEM
    "21BE45": 2,    # BIOLOGY FOR ENGINEERS
    "21CSL46": 1,   # PYTHON PROGRAMMING LABORATORY
    "21CIP47": 1,   # CONSTITUTION OF INDIA & PROFESSIONAL ETHICS
    "21UH49": 1,    # UNIVERSAL HUMAN VALUES AND PROFESSIONAL ETHICS
    "21INT49": 2,   # INTER/INTRA INSTITUTIONAL INTERNSHIP
    # Semester 5
    "21CS51": 3,    # AUTOMATA THEORY AND COMPILER DESIGN
    "21CSL582": 1,  # C# PROGRAMMING
    "21CS52": 4,    # COMPUTER NETWORKS
    "21CS53": 3,    # DATABASE MANAGEMENT SYSTEMS
    "21CS54": 3,    # ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING
    "21CSL55": 1,   # DATABASE MANAGEMENT SYSTEMS LABORATORY WITH MINI PROJECT
    "21RMI56": 2,   # RESEARCH METHODOLOGY & INTELLECTUAL PROPERTY RIGHTS
    "21CIV57": 1,   # ENVIRONMENTAL STUDIES
    # Semester 6
    "21CS61": 3,    # SOFTWARE ENGINEERING AND PROJECT MANAGEMENT
    "21CS62": 4,    # FULL STACK DEVELOPMENT
    "21CS642": 3,   # ADVANCED JAVA PROGRAMMING
    "21CS63": 3,    # COMPUTER GRAPHICS AND FUNDAMENTALS OF IMAGE PROCESSING
    "21CSL66": 1,   # COMPUTER GRAPHICS AND IMAGE PROCESSING LABORATORY
    "21CSMP67": 2,  # MINI PROJECT
    "21INT68": 3,   # SOCIETAL INTERNSHIP
    "21ME651": 3,   # PROJECT MANAGEMENT
    # Semester 7
    "21CS71": 3,    # BIG DATA ANALYTICS
    "21CS72": 2,    # CLOUD COMPUTING
    "21CV753": 3,   # ENVIRONMENTAL PROTECTION AND MANAGEMENT
    "21CS734": 3,   # BLOCKCHAIN TECHNOLOGY
    "21CS745": 3,   # NOSQL DATABASE
}

SEMESTERS_TOTAL_CREDITS = [
    0, 20, 20, 18, 22, 18, 22, 14, 0
]

SEMESTERS_SUBJECTS = [
    {},
    {"21MAT11","21PHY12","21ELE13","21CIV14","21EVN15","21PHYL16","21ELEL17","21EGH18","21IDT19"},
    {"21MAT21","21CHE22","21PSP23","21ELN24","21EME25","21CHEL26","21CPL27","21EGH28","21SFH29"},
    {"21MAT31","21CS32","21CS382","21CS33","21CS34","21CSL35","21SCR36","21KSK37"},
    {"21MATCS41","21CS42","21CSL483","21CS43","21CS44","21BE45","21CSL46","21CIP47","21UH49","21INT49"},
    {"21CS51","21CSL582","21CS52","21CS53","21CS54","21CSL55","21RMI56","21CIV57"},
    {"21CS61","21CS62","21CS642","21CS63","21CSL66","21CSMP67","21INT68","21ME651"},
    {"21CS71","21CS72","21CV753","21CS734","21CS745"}
]

def get_grade_point(marks):
    if marks >= 90:
        return 10
    elif marks >= 80:
        return 9
    elif marks >= 70:
        return 8
    elif marks >= 60:
        return 7
    elif marks >= 55:
        return 6
    elif marks >= 50:
        return 5
    elif marks >= 40:
        return 4
    else:
        return 0

def get_semester(subject_code):
    for i in range(1, NUMBER_OF_SEMESTERS + 1):
        if subject_code in SEMESTERS_SUBJECTS[i]:
            return i

def calculate_cgpa_from_pdfs(pdf_paths):
    semesters_calculated_total = [0] * (NUMBER_OF_SEMESTERS + 1)
    detailed_results = {i: [] for i in range(1, NUMBER_OF_SEMESTERS + 1)}
    for pdf_path in pdf_paths:
        print(f"Processing PDF: {pdf_path}")
        tables = camelot.read_pdf(pdf_path, flavor='stream')
        for j in range(0, len(tables)):
            df = tables[j].df
            print(f"Table {j} DataFrame:\n{df}")
            if df.iloc[0, 0] == 'University Seat Number':
                continue
            for k in range(1, len(df)):  # skip header row
                row = df.iloc[k]
                subject_code = row[0]
                subject_name = row[1] if len(row) > 1 else ""
                if subject_code not in SUBJECT_CODE_CREDITS:
                    continue
                credits = SUBJECT_CODE_CREDITS[subject_code]
                total = row[4]
                try:
                    marks = int(total)
                except ValueError:
                    continue
                current_semester = get_semester(subject_code)
                grade_point = get_grade_point(marks)
                semesters_calculated_total[current_semester] += grade_point * credits
                detailed_results[current_semester].append({
                    "subject_code": subject_code,
                    "subject_name": subject_name,
                    "marks": marks,
                    "credits": credits,
                    "grade_point": grade_point
                })
    print(f"Detailed results: {json.dumps(detailed_results, indent=2)}")
    total_valid_semesters = 0
    total_sgpa = 0
    sgpas = []
    for i in range(1, NUMBER_OF_SEMESTERS + 1):
        if SEMESTERS_TOTAL_CREDITS[i] == 0 or semesters_calculated_total[i] == 0:
            sgpas.append(None)
            continue
        total_valid_semesters += 1
        sgpa = semesters_calculated_total[i] / SEMESTERS_TOTAL_CREDITS[i]
        total_sgpa += sgpa
        sgpas.append(sgpa)
    cgpa = total_sgpa / total_valid_semesters if total_valid_semesters > 0 else 0
    return {
        "cgpa": cgpa,
        "sgpas": sgpas,
        "semesters": detailed_results
    } 