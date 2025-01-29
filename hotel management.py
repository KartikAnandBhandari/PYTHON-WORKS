# HOTEL MANAGEMENT SYSTEM

def display_menu():
    print("1. Add employee")
    print("2. Remove employee")
    print("3. Display all employees")
    print("4. Exit")

def add_employee(employees):
    name = input("Enter employee name: ")
    position = input("Enter employee position: ")
    salary = float(input("Enter employee salary: "))
    employees.append({"name": name, "position": position, "salary": salary})
    print("Employee added successfully!")

def remove_employee(employees):
    name = input("Enter name of employee to remove: ")
    for employee in employees:
        if employee["name"] == name:
            employees.remove(employee)
            print("Employee removed successfully!")
            return
    print("Employee not found.")

def display_employees(employees):
    if not employees:
        print("No employees to display.")
    else:
        print("Employee list:")
        for employee in employees:
            print(f"Name: {employee['name']}, Position: {employee['position']}, Salary: {employee['salary']}")

def main():
    employees = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            remove_employee(employees)
        elif choice == "3":
            display_employees(employees)
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()