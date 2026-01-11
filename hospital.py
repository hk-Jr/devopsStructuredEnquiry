
patients = {}

# Add base patients
patients["P1"] = {
    "name": "Amit Sharma",
    "age": 30,
    "disease": "Flu"
}

patients["P2"] = {
    "name": "Neha Verma",
    "age": 25,
    "disease": "Migraine"
}


def get_patient_summary(patient_id):
    patient = patients.get(patient_id)

    if patient is None:
        return "Patient not found"

    return (
        f"Patient ID: {patient_id}\n"
        f"Name: {patient['name']}\n"
        f"Age: {patient['age']}\n"
        f"Disease: {patient['disease']}"
    )

if __name__ == "__main__":
    print("HOSPITAL MANAGEMENT SYSTEM\n")

    print("Fetching Patient P1 details:\n")
    print(get_patient_summary("P1"))

    print("\nFetching Patient P2 details:\n")
    print(get_patient_summary("P2"))

    print("\nFetching unknown patient:\n")
    print(get_patient_summary("P99"))
