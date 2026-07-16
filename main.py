from employee import *
from student import *

while True:

    print("\n========== COLLEGE DATABASE ==========")
    print("1. Employee Database")
    print("2. Student Database")
    print("3. Exit")

    try:
        main_choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid Choice!")
        continue

    match main_choice:

        case 1:

            while True:

                print("\n===== Employee CRUD Operations =====")
                print("1. Add Employee")
                print("2. View Employees")
                print("3. Update Employee")
                print("4. Delete Employee")
                print("5. Back")

                try:
                    choice = int(input("Enter your choice: "))
                except ValueError:
                    print("Invalid Choice!")
                    continue

                match choice:

                    case 1:
                        add_employee()

                    case 2:
                        read_employee()

                    case 3:
                        update_employee()

                    case 4:
                        delete_employee()

                    case 5:
                        break

                    case _:
                        print("Invalid Choice!")

        case 2:

            while True:

                print("\n===== Student CRUD Operations =====")
                print("1. Add Student")
                print("2. View Students")
                print("3. Update Student")
                print("4. Delete Student")
                print("5. Back")

                try:
                    choice = int(input("Enter your choice: "))
                except ValueError:
                    print("Invalid Choice!")
                    continue

                match choice:

                    case 1:
                        add_student()

                    case 2:
                        read_student()

                    case 3:
                        update_student()

                    case 4:
                        delete_student()

                    case 5:
                        break

                    case _:
                        print("Invalid Choice!")

        case 3:
            print("Thank You!")
            break

        case _:
            print("Invalid Choice!")