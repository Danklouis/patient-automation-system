import pandas as pd

# 🔹 File paths (clean and reusable)
INPUT_FILE = "data/patients.txt"
OUTPUT_FILE = "output/patients_output.xlsx"


def main():
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
            continue  # skip invalid rows

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
            print(f"⚠️ Unknown modality detected: {procedure}")

        # 🔹 Store record
        records.append({
            "Name": name,
            "Age": age,
            "Category": category,
            "Modality": modality,
            "Procedure": procedure
        })

    # 🔹 Create DataFrame
    df = pd.DataFrame(records)

    # 🔹 Check if empty
    if df.empty:
        print("⚠️ No valid data found.")
        return

    # 🔹 Sort data
    df = df.sort_values(by=["Modality", "Age"]).reset_index(drop=True)

    # 🔹 Export to Excel
    try:
        with pd.ExcelWriter(OUTPUT_FILE) as writer:

            # Write each modality sheet
            for modality, group in df.groupby("Modality"):
                group = group.sort_values(by="Age")
                group.to_excel(writer, sheet_name=modality, index=False)

            # Summary sheet
            summary = df["Modality"].value_counts().reset_index()
            summary.columns = ["Modality", "Count"]
            summary.to_excel(writer, sheet_name="Summary", index=False)

    except Exception as e:
        print(f"❌ Error writing Excel file: {e}")
        return

    print("✅ Data exported with modality grouping")


# 🔹 Entry point (important for Python projects)
if __name__ == "__main__":
    main()