import sys
from database import Database
from employee import Employee

def main():
    if len(sys.argv) < 2:
        print("Usage: myApp <mode> [parameters]")
        return
    
    mode = sys.argv[1]
    db = Database()

    if mode == "1":
        # Create the employees table
        db.create_table()
    elif mode == "2":
        # Insert a new employee
        if len(sys.argv) < 5:
            print("Usage: myApp 2 <full_name> <birth_date> <gender>")
            return
        full_name = sys.argv[2]
        birth_date = sys.argv[3]
        gender = sys.argv[4]
        employee = Employee(full_name, birth_date, gender)
        db.insert_employee(employee)
    elif mode == "3":
        # Print all employees, sorted by full name
        db.print_employees()
    elif mode == "4":
        # Bulk insert of 1,000,000 employees
        db.bulk_insert_employees()
    elif mode == "5":
        # Find employees by specific criteria
        db.find_employees_by_criteria()
    elif mode == "6":
        # Optimize the database
        db.optimize_database()

from database import Database

if __name__ == "__main__":
    db = Database()
    while True:
        print("Choose an action:")
        print("1: Create Table")
        print("2: Insert Employee")
        print("3: Print Employees")
        print("4: Bulk Insert Employees")
        print("5: Find Male Employees with Last Name Starting with 'F'")
        print("6: Optimize Database")
        print("0: Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            db.create_table()
        elif choice == '2':
            full_name = input("Enter full name: ")
            birth_date = input("Enter birth date (YYYY-MM-DD): ")
            gender = input("Enter gender: ")
            employee = Employee(full_name, birth_date, gender)
            db.insert_employee(employee)
        elif choice == '3':
            db.print_employees()
        elif choice == '4':
            db.bulk_insert_employees()
        elif choice == '5':
            db.find_employees_by_criteria()
        elif choice == '6':
            db.optimize_database()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")
