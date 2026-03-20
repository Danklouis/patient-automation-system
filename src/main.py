import pandas as pd
import argparse
import logging


def get_args():
    parser = argparse.ArgumentParser(description="Patient Automation System")
    parser.add_argument(
        "--input",
        type=str,
        default="data/patients.txt",
        help="Path to input file"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="output/patients_output.xlsx",
        help="Path to output Excel file"
    )
    return parser.parse_args()


def main():
    # 🔹 Get CLI arguments
    args = get_args()
    INPUT_FILE = args.input
    OUTPUT_FILE = args.output

    # 🔹 Setup logging
    logging.basicConfig(
        filename="output/process.log",
        level=logging.WARNING,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    records = []

    # 🔹 Read file
    try:
        with open(INPUT_FILE, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"❌ File not found: {INPUT_FILE}")
        return

    # 🔹 Process each line
    for line in lines:
        try:
            name, age, procedure = line.strip().split(",")
            age = int(age)
        except ValueError:
            continue

        # 🔹 Category logic
        if age <= 18:
            category = "Pediatric"
        elif age >= 60:
            category = "Senior"
        else:
            category = "Adult"

        # 🔹 Modality detection
        procedure_lower = procedure.lower()

        if "x-ray" in procedure_lower:
            modality = "X-Ray"
        elif "mri" in procedure_lower:
            modality = "MRI"
        elif "ct scan" in procedure_lower:
            modality = "CT Scan"
        elif "ultrasound" in procedure_lower:
            modality = "Ultrasound"
            
        else:
            modality = "Other"

        # 🔹 Log unknown modality
        if modality == "Other":
            logging.warning(f"Unknown modality detected: {procedure}")

        # 🔹 Store record
        records.append({
            "Name": name,
            "Age": age,
            "Category": category,
            "Modality": modality,
            "Procedure": procedure
        })

    df = pd.DataFrame(records)

    if df.empty:
        print("⚠️ No valid data found.")
        return

    df = df.sort_values(by=["Modality", "Age"]).reset_index(drop=True)

    # 🔹 Export
    try:
        with pd.ExcelWriter(OUTPUT_FILE) as writer:
            for modality, group in df.groupby("Modality"):
                group = group.sort_values(by="Age")
                group.to_excel(writer, sheet_name=modality, index=False)

            summary = df["Modality"].value_counts().reset_index()
            summary.columns = ["Modality", "Count"]
            summary.to_excel(writer, sheet_name="Summary", index=False)

    except Exception as e:
        print(f"❌ Error writing Excel file: {e}")
        return

    print("✅ Data exported with modality grouping")


if __name__ == "__main__":
    main()