import csv
import student


def csv_convert():

    students = student.read_student()

    if students is None:
        print("No student data.")
        return

    if len(students) == 0:
        print("Student data is empty.")
        return

    with open("student.csv", "w", newline="") as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow([
            "Student ID",
            "Student Name",
            "Department",
            "CGPA",
            "Fees"
        ])

        for stu in students:

            writer.writerow([
                stu[0],
                stu[1],
                stu[2],
                stu[3],
                stu[4]
            ])

    print("Student data successfully exported to student.csv")


if __name__ == "__main__":
    csv_convert()