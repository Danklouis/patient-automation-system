# 🏥 Patient Automation System

A Python-based automation tool that processes patient data and generates structured Excel reports with modality-based categorization.

## 🧠 Problem Solved

Manual patient data encoding and report generation is time-consuming and error-prone.  
This system automates classification, categorization, and reporting of patient imaging data.

---

## 🚀 Features

- 📂 Reads patient data from text file
- 🧠 Automatically categorizes patients:
  - Pediatric
  - Adult
  - Senior
- 🩻 Detects imaging modality:
  - X-Ray
  - MRI
  - CT Scan
  - Ultrasound
- 📊 Generates Excel report with:
  - Separate sheets per modality
  - Summary sheet with counts
- ⚠️ Handles invalid data gracefully

---

## 📁 Project Structure

```
patient-automation-system/
│
├── data/                # Input data
├── output/              # Generated Excel files
├── src/                 # Source code
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/patient-automation-system.git
cd patient-automation-system
```

2. Create virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the script:

```bash
python src/main.py --input data/patients.txt
```

---

## 📊 Sample Output

- Excel file with:
  - Multiple sheets (by modality)
  - Summary report
 
<img width="577" height="1007" alt="image" src="https://github.com/user-attachments/assets/64fd8638-8eed-4234-85fc-b53f031eca64" /><img width="432" height="386" alt="image" src="https://github.com/user-attachments/assets/5e05f199-47c3-4beb-94f3-29f04e46d53d" />


## 👨‍💻 Author

Danklouis
>>>>>>> f06b07e (Add CLI support, logging system, and improved project structure)
