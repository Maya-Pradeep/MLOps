from sql import execute


def add_student():

    print("\n----- Add Student -----")

    name = input("Enter Student Name: ")

    department = input("Enter Department (CSE/ECE/EEE): ").upper()

    try:
        cgpa = float(input("Enter CGPA: "))
    except ValueError:
        print("Invalid CGPA")
        return

    try:
        fees = float(input("Enter Course Fees: "))
    except ValueError:
        print("Invalid Fees")
        return

    query = """
    INSERT INTO student
    (name, department, cgpa, fees)
    VALUES(?,?,?,?)
    """

    rows = execute(
        query,
        (name, department, cgpa, fees)
    )

    if rows:
        print("Student Added Successfully!")
    else:
        print("Student Not Added!")


def read_student():

    students = execute("SELECT * FROM student")

    if students:

        print("\nStudent Records")
        print("-"*80)

        print(
            f"{'ID':<8}"
            f"{'Name':<20}"
            f"{'Department':<15}"
            f"{'CGPA':<10}"
            f"{'Fees':<15}"
        )

        print("-"*80)

        for student in students:

            print(
                f"{student[0]:<8}"
                f"{student[1]:<20}"
                f"{student[2]:<15}"
                f"{student[3]:<10}"
                f"{student[4]:<15}"
            )

    else:
        print("No Students Found.")

    return students


def update_student():

    try:
        student_id = int(input("Enter Student ID: "))
    except ValueError:
        print("Invalid Student ID")
        return

    check = execute(
        "SELECT * FROM student WHERE id=?",
        (student_id,)
    )

    if not check:
        print("Student Not Found.")
        return

    department = input("Enter New Department: ").upper()

    try:
        cgpa = float(input("Enter New CGPA: "))
    except ValueError:
        print("Invalid CGPA")
        return

    try:
        fees = float(input("Enter New Fees: "))
    except ValueError:
        print("Invalid Fees")
        return

    query = """
    UPDATE student

    SET department=?,
        cgpa=?,
        fees=?

    WHERE id=?
    """

    rows = execute(
        query,
        (department, cgpa, fees, student_id)
    )

    if rows:
        print("Student Updated Successfully!")
    else:
        print("Student Not Updated!")


def delete_student():

    try:
        student_id = int(input("Enter Student ID: "))
    except ValueError:
        print("Invalid Student ID")
        return

    rows = execute(
        "DELETE FROM student WHERE id=?",
        (student_id,)
    )

    if rows:
        print("Student Deleted Successfully!")
    else:
        print("Student Not Found.")