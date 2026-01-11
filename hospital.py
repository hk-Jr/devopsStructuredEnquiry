# ============================================
#  Hospital Appointment & Patient Record System
#  MAIN BRANCH – Base Prototype
# ============================================

print("HOSPITAL MANAGEMENT SYSTEM\n")

# Data storage
patients = {}
appointments = {}

# ----------------------------
# Adding patients (base data)
# ----------------------------

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

print("Patients added to system.\n")

# ----------------------------
# Display all patients
# ----------------------------

print("Patient Records:")
print("----------------")

print("ID: P1")
print("Name:", patients["P1"]["name"])
print("Age:", patients["P1"]["age"])
print("Disease:", patients["P1"]["disease"])
print()

print("ID: P2")
print("Name:", patients["P2"]["name"])
print("Age:", patients["P2"]["age"])
print("Disease:", patients["P2"]["disease"])
print()

# ----------------------------
# System status
# ----------------------------

print("System Status: Hospital system is running.")
