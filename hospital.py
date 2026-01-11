# Hospital Management System - Base Version (Main Branch)

print("===================================")
print("  HOSPITAL MANAGEMENT SYSTEM")
print("===================================")

def system_status():
    return "System is running"

def show_menu():
    print("\nMain Menu")
    print("1. Check system status")
    print("2. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            print("\nStatus:", system_status())

        elif choice == "2":
            print("\nExiting system...")
            break

        else:
            print("\nInvalid option. Try again.")

if __name__ == "__main__":
    main()
