# 🏥 Patient Automation System

A Python-based automation tool that processes patient data and generates structured Excel reports with modality-based categorization.

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
python src/main.py
```

---

## 📊 Sample Output

- Excel file with:
  - Multiple sheets (by modality)
  - Summary report

---

## 👨‍💻 Author

Danklouis
