from sql import execute


def add_employee():

    print("\n----- Add Employee -----")

    try:
        emp_id = int(input("Enter Employee ID: "))
    except ValueError:
        print("Invalid Employee ID")
        return

    name = input("Enter Employee Name: ")

    department = input("Enter Department (CSE/ECE/EEE): ").upper()

    try:
        salary = float(input("Enter Salary: "))
    except ValueError:
        print("Invalid Salary")
        return

    try:
        capacity = int(input("Enter Mentor Capacity: "))
    except ValueError:
        print("Invalid Capacity")
        return

    query = """
    INSERT INTO employee
    (employee_id, employee_name, department, salary, mentor_capacity)
    VALUES(?,?,?,?,?)
    """

    rows = execute(
        query,
        (emp_id, name, department, salary, capacity)
    )

    if rows:
        print("Employee Added Successfully!")
    else:
        print("Employee Not Added!")


def read_employee():

    query = "SELECT * FROM employee"

    employees = execute(query)

    if employees:

        print("\nEmployee Records")
        print("-" * 90)

        print(
            f"{'ID':<8}"
            f"{'Name':<20}"
            f"{'Department':<15}"
            f"{'Salary':<15}"
            f"{'Capacity':<10}"
        )

        print("-" * 90)

        for employee in employees:

            print(
                f"{employee[0]:<8}"
                f"{employee[1]:<20}"
                f"{employee[2]:<15}"
                f"{employee[3]:<15}"
                f"{employee[4]:<10}"
            )

    else:
        print("No Employees Found.")

    return employees


def update_employee():

    try:
        emp_id = int(input("Enter Employee ID: "))
    except ValueError:
        print("Invalid Employee ID")
        return

    check = execute(
        "SELECT * FROM employee WHERE employee_id=?",
        (emp_id,)
    )

    if not check:
        print("Employee Not Found.")
        return

    name = input("Enter New Name: ")

    department = input("Enter New Department: ").upper()

    try:
        salary = float(input("Enter New Salary: "))
    except ValueError:
        print("Invalid Salary")
        return

    try:
        capacity = int(input("Enter New Mentor Capacity: "))
    except ValueError:
        print("Invalid Capacity")
        return

    query = """
    UPDATE employee

    SET employee_name=?,
        department=?,
        salary=?,
        mentor_capacity=?

    WHERE employee_id=?
    """

    rows = execute(
        query,
        (name, department, salary, capacity, emp_id)
    )

    if rows:
        print("Employee Updated Successfully!")
    else:
        print("Employee Not Updated!")


def delete_employee():

    try:
        emp_id = int(input("Enter Employee ID: "))
    except ValueError:
        print("Invalid Employee ID")
        return

    rows = execute(
        "DELETE FROM employee WHERE employee_id=?",
        (emp_id,)
    )

    if rows:
        print("Employee Deleted Successfully!")
    else:
        print("Employee Not Found.")