# ============================================
#  Hospital Appointment & Patient Record System
#  MAIN BRANCH
# ============================================

# Data storage
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

# --------------------------------
# Function to return formatted data
# --------------------------------
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
