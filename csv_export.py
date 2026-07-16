import csv
import employee


def csv_convert():

    employees = employee.read_employee()

    if employees is None:
        print("No employee data.")
        return

    if len(employees) == 0:
        print("Employee data is empty.")
        return

    with open("employee.csv", "w", newline="") as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow([
            "Employee ID",
            "Employee Name",
            "Department",
            "Employee Salary",
            "Mentor Capacity"
        ])

        for emp in employees:

            writer.writerow([
                emp[0],
                emp[1],
                emp[2],
                emp[3],
                emp[4]
            ])

    print("Employee data successfully exported to employee.csv")


if __name__ == "__main__":
    csv_convert()