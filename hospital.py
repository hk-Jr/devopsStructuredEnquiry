# =====================================================
#  Hospital Appointment & Patient Record Management
#  MAIN BRANCH (Stable Base)
# =====================================================

print("\n======================================")
print("   HOSPITAL MANAGEMENT SYSTEM")
print("======================================")

# -------------------------------
# In-memory storage (empty now)
# -------------------------------
patients = {}
appointments = {}

# -------------------------------
# Utility Functions
# -------------------------------

def generate_patient_id():
    return f"P{len(patients) + 1}"

def generate_appointment_id():
    return f"A{len(appointments) + 1}"

# -------------------------------
# System Functions
# -------------------------------

def system_status():
    return "Hospital System Running"

# -------------------------------
# Patient Module (BASE)
# -------------------------------

def patient_menu():
    print("\n--- Patient Management ---")
    print("1. Register Patient (Not Implemented)")
    print("2. View Patients (Not Implemented)")
    print("3. Back")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\nPatient registration will be added in feature-patients branch")

    elif choice == "2":
        print("\nPatient viewing will be added in feature-patients branch")

    elif choice == "3":
        return
    else:
        print("\nInvalid choice")

# -------------------------------
# Appointment Module (BASE)
# -------------------------------

def appointment_menu():
    print("\n--- Appointment Management ---")
    print("1. Book Appointment (Not Implemented)")
    print("2. View Appointments (Not Implemented)")
    print("3. Back")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\nAppointment booking will be added in feature-appointments branch")

    elif choice == "2":
        print("\nAppointment viewing will be added in feature-appointments branch")

    elif choice == "3":
        return
    else:
        print("\nInvalid choice")

# -------------------------------
# Main Menu
# -------------------------------

def main_menu():
    print("\n====== Main Menu ======")
    print("1. System Status")
    print("2. Patient Management")
    print("3. Appointment Management")
    print("4. Exit")

# -------------------------------
# Program Entry
# -------------------------------

def main():
    while True:
        main_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            print("\nStatus:", system_status())

        elif choice == "2":
            patient_menu()

        elif choice == "3":
            appointment_menu()

        elif choice == "4":
            print("\nExiting Hospital System...")
            break

        else:
            print("\nInvalid option. Try again.")

# Start system
if __name__ == "__main__":
    main()
