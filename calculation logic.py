import camelot
import json
import os
from pprint import pprint

NUMBER_OF_SEMESTERS = 8

"""
TODO: Add other subjects that one could opt for
"""
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
    "21INT49": 2,   # INTER\/INTRA INSTITUTIONAL INTERNSHIP

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

"""
TODO: Learn to calculate SGPA for semester 8 and replace dummy with actual value 
"""
SEMESTERS_TOTAL_CREDITS = [
    0,      # Dummy Semester 0
    20,     # Semester 1
    20,     # Semester 2
    18,     # Semester 3
    22,     # Semester 4
    18,     # Semester 5
    22,     # Semester 6
    14,     # Semester 7
    0,     # Dummy Semester 8
]

SEMESTERS_SUBJECTS = [
    {
        # Dummy Semester 0
    },
    {
        # Semester 1
        "21MAT11",
        "21PHY12",
        "21ELE13",
        "21CIV14",
        "21EVN15",
        "21PHYL16",
        "21ELEL17",
        "21EGH18",
        "21IDT19"
    },
    {
        # Semester 2
        "21MAT21",
        "21CHE22",
        "21PSP23",
        "21ELN24",
        "21EME25",
        "21CHEL26",
        "21CPL27",
        "21EGH28",
        "21SFH29"
    },
    {
        # Semester 3
        "21MAT31",
        "21CS32",
        "21CS382",
        "21CS33",
        "21CS34",
        "21CSL35",
        "21SCR36",
        "21KSK37"
    },
    {
        # Semester 4
        "21MATCS41",
        "21CS42",
        "21CSL483",
        "21CS43",
        "21CS44",
        "21BE45",
        "21CSL46",
        "21CIP47",
        "21UH49",
        "21INT49"
    },
    {
        # Semester 5
        "21CS51",
        "21CSL582",
        "21CS52",
        "21CS53",
        "21CS54",
        "21CSL55",
        "21RMI56",
        "21CIV57"
    },
    {
        # Semester 6
        "21CS61",
        "21CS62",
        "21CS642",
        "21CS63",
        "21CSL66",
        "21CSMP67",
        "21INT68",
        "21ME651"
    },
    {
        # Semester 7
        "21CS71",
        "21CS72",
        "21CV753",
        "21CS734",
        "21CS745"
    }
]

"""
TODO: Handle fail case in marks calculation
If the student has failed in the subject, he might have passed it in 
a future semester and that has to be considered accordingly. 
Not entirely sure how this works, needs discussion
""" 
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
    else:               # FAIL 
        return 0

def get_semester(subject_code):
    for i in range(1, NUMBER_OF_SEMESTERS + 1):
        if subject_code in SEMESTERS_SUBJECTS[i]:
            return i
    

"""
TODO: Take path input from the user
Handle case where path does not exist
"""
pdf_dir_path = r"/workspaces/python-3/results"

pdf_paths = []

"""
TODO: Write a check to ensure only pdfs are considered to exclude invalid formats such as .csv, .txt etc
Also, ensure that the pdf can indeed be processed to get the results (The pdf should have vtu results)
"""
for file in os.listdir(pdf_dir_path):
    pdf_path = os.path.join(pdf_dir_path, file)
    pdf_paths.append(pdf_path)
    # print(pdf_path)

"""
TODO: Remove later, sorting is an overhead
Keeping this line for now just for predictability of the flow of program
""" 
pdf_paths.sort()

# Index 0 is a dummy
semesters_calculated_total = [0] * (NUMBER_OF_SEMESTERS + 1)

for i in range(0, len(pdf_paths)):
    tables = camelot.read_pdf(pdf_paths[i])

    # We iterate from index 1 and not 0 as the 0th table holds only USN and Name, not the results
    for j in range(0, len(tables)):
        json_file_path = f"/workspaces/python-3/table-{i}.json"

        # Skip the table if it is a table that holds USN and Name (Because this table does not hold marks)
        if tables[j].df[0][0] == 'University Seat Number':
            continue
        tables[j].to_json(json_file_path)

        with open(json_file_path) as file:
            parsed_json = json.load(file)
            # pprint(parsed_json)

            for k in range(0, len(parsed_json)):
                """
                TODO: Maybe use a different identifier?
                What if the 'Total' column is not at '4'?
                """
                # Skip the table header row
                if parsed_json[k]['4'] == 'Total':
                    continue

                subject_code = parsed_json[k]['0']

                if subject_code not in SUBJECT_CODE_CREDITS:
                    continue

                subject_name = parsed_json[k]['1'] 
                credits = SUBJECT_CODE_CREDITS[subject_code]
                total = parsed_json[k]['4']
                # print(f"{subject_name} ({credits}): {total}")

                current_semester = get_semester(subject_code)
                grade_point = get_grade_point(int(total))
                semesters_calculated_total[current_semester] += grade_point * credits


total_valid_semesters = 0
total_sgpa = 0

print("--------------SGPA--------------------")
for i in range(1, NUMBER_OF_SEMESTERS + 1):
    # If credits for a semester is not hardcoded with valid value or if there were no subjects present for result calculation in a particular semester
    if SEMESTERS_TOTAL_CREDITS[i] == 0 or semesters_calculated_total[i] == 0:
        continue
    
    total_valid_semesters += 1
    sgpa = semesters_calculated_total[i] / SEMESTERS_TOTAL_CREDITS[i]
    total_sgpa += sgpa
    print(f"Semester {i}: {sgpa}")

print("--------------------------")

cgpa = total_sgpa / total_valid_semesters
print(f"CGPA: {cgpa}")